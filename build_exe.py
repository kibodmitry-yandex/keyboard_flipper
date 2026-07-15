"""
Build script for keyboard_flipper - creates portable standalone EXE
Run: python build_exe.py
"""

import subprocess
import sys
from pathlib import Path
from shutil import copy2
from PIL import Image


def ensure_icon(repo_path: Path) -> Path:
    png = repo_path / 'icon.png'
    ico = repo_path / 'icon.ico'
    if not png.exists():
        print('icon.png not found — creating placeholder')
        img = Image.new('RGBA', (64, 64), (0, 122, 204, 255))
        from PIL import ImageDraw
        d = ImageDraw.Draw(img)
        d.text((12, 18), 'KF', fill='white')
        img.save(png)
    try:
        img = Image.open(png)
        img.save(ico, format='ICO')
        print(f'Wrote {ico}')
    except Exception as e:
        print('Failed to create ICO from PNG:', e)
    return ico


def build_exe():
    """Build EXE using PyInstaller; convert icon and copy sidecar config into dist."""
    repo_path = Path(__file__).parent
    script = repo_path / "keyboard_flipper.py"
    output_dir = repo_path / "dist"

    if not script.exists():
        print(f"❌ Script not found: {script}")
        return False

    # Check if PyInstaller is installed
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("❌ PyInstaller not installed")
        print("Run: pip install pyinstaller pillow pystray")
        return False

    ico = ensure_icon(repo_path)

    # PyInstaller command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--noconsole",
        "--name",
        "keyboard_flipper",
        "--icon",
        str(ico),
        "--distpath",
        str(output_dir),
        "--workpath",
        str(repo_path / "build"),
        "--specpath",
        str(repo_path),
        str(script),
    ]

    print("🔨 Building EXE...")
    print(f"   Command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)

        if result.returncode == 0:
            exe_path = output_dir / "keyboard_flipper.exe"
            print(f"✅ Build successful!")
            print(f"   EXE: {exe_path}")
            try:
                print(f"   Size: {exe_path.stat().st_size / 1024 / 1024:.1f} MB")
            except Exception:
                pass
            # Ensure only EXE and config remain in dist
            cfg = repo_path / 'keyboard_flipper_config.json'
            target_cfg = output_dir / 'keyboard_flipper_config.json'
            if cfg.exists():
                if not target_cfg.exists():
                    try:
                        copy2(cfg, target_cfg)
                        print(f'Copied config to {target_cfg}')
                    except Exception as e:
                        print('Failed to copy config:', e)
            else:
                # No repo config — create default config inside dist using keyboard_flipper.DEFAULT_CONFIG if possible
                try:
                    import importlib.util
                    spec = importlib.util.spec_from_file_location('kf', str(repo_path / 'keyboard_flipper.py'))
                    if spec is not None and spec.loader is not None:
                        kf = importlib.util.module_from_spec(spec)
                        # type: ignore[arg-type]
                        spec.loader.exec_module(kf)  # loader is not None here
                        default = getattr(kf, 'DEFAULT_CONFIG', None)
                        if default is not None:
                            import json as _json
                            target_cfg.write_text(_json.dumps(default, ensure_ascii=False, indent=2), encoding='utf-8')
                            print(f'Created default config at {target_cfg}')
                    else:
                        print('Could not load keyboard_flipper module to extract DEFAULT_CONFIG')
                except Exception as e:
                    print('Failed to create default config in dist:', e)

            # Remove leftover icon files and logs from dist, keep only exe and config
            for name in ('icon.png', 'icon.ico', 'keyboard_flipper.log'):
                f = output_dir / name
                try:
                    if f.exists():
                        f.unlink()
                        print(f'Removed {f} from dist')
                except Exception:
                    pass

            return True
        else:
            print("❌ Build failed!")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
