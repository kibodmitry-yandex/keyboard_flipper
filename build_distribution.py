"""
Build complete Keyboard Flipper distribution package
Creates folder with standalone EXE and all necessary files
"""

import shutil
import subprocess
import sys
from pathlib import Path


def build_distribution():
    """Build complete distribution package"""
    repo_path = Path(__file__).parent
    dist_name = "KeyboardFlipper_Portable"
    dist_path = repo_path / dist_name
    
    print("\n" + "="*60)
    print("🔨 Building Keyboard Flipper Distribution Package")
    print("="*60 + "\n")
    
    # Step 1: Clean old distribution
    print("📋 Step 1: Cleaning old distribution...")
    if dist_path.exists():
        shutil.rmtree(dist_path)
        print(f"   ✅ Removed old: {dist_path}")
    
    # Step 2: Create distribution folder
    print("\n📋 Step 2: Creating distribution folder...")
    dist_path.mkdir(exist_ok=True)
    print(f"   ✅ Created: {dist_path}")
    
    # Step 3: Copy EXE
    print("\n📋 Step 3: Copying EXE file...")
    exe_source = repo_path / "dist" / "KeyboardFlipper.exe"
    if not exe_source.exists():
        print(f"   ❌ EXE not found: {exe_source}")
        print("   Build it first with: python build_exe.py")
        return False
    
    exe_dest = dist_path / "KeyboardFlipper.exe"
    shutil.copy2(exe_source, exe_dest)
    exe_size_mb = exe_dest.stat().st_size / 1024 / 1024
    print(f"   ✅ Copied: KeyboardFlipper.exe ({exe_size_mb:.1f} MB)")
    
    # Step 4: Copy config template
    print("\n📋 Step 4: Copying configuration template...")
    config_source = repo_path / "keyboard_flipper_config.json"
    config_dest = dist_path / "keyboard_flipper_config.json"
    shutil.copy2(config_source, config_dest)
    print(f"   ✅ Copied: keyboard_flipper_config.json")
    
    # Step 5: Copy batch files
    print("\n📋 Step 5: Copying launcher scripts...")
    bat_files = ["run_keyboard_flipper.bat", "setup_autostart.bat"]
    for bat in bat_files:
        bat_source = repo_path / bat
        if bat_source.exists():
            bat_dest = dist_path / bat
            shutil.copy2(bat_source, bat_dest)
            print(f"   ✅ Copied: {bat}")
    
    # Step 6: Create README.txt in distribution
    print("\n📋 Step 6: Creating README...")
    readme_content = """================================================================================
                    🎹 KEYBOARD FLIPPER - Portable Edition
================================================================================

БЫСТРЫЙ СТАРТ:
1. Откройте run_keyboard_flipper.bat
2. Приложение появится в системном трее
3. Нажимайте Ctrl+Shift+F для переворота раскладки выделенного текста

ФАЙЛЫ:
- KeyboardFlipper.exe              ← Главное приложение
- keyboard_flipper_config.json     ← Конфигурация
- run_keyboard_flipper.bat         ← Быстрый запуск
- setup_autostart.bat              ← Добавление в автозагрузку
- README.txt                       ← Этот файл

ТРЕБОВАНИЯ:
- Windows 7 или выше
- Никаких зависимостей - всё уже включено!

КАК ЭТО РАБОТАЕТ:
1. Выделите текст, набранный не на той раскладке
2. Нажмите Ctrl+Shift+F (горячая клавиша)
3. Текст автоматически переведётся в правильную раскладку
4. Выбранный текст заменится на переведённый

КАСТОМИЗАЦИЯ:
Отредактируйте keyboard_flipper_config.json для изменения:
- Горячей клавиши (по умолчанию: ctrl+shift+f)
- Типа раскладки (по умолчанию: ru_us)

ПРИМЕРЫ ГОРЯЧИХ КЛАВИШ:
- ctrl+shift+f (по умолчанию)
- alt+shift+x
- ctrl+alt+f
- f12
- win+k

АВТОЗАГРУЗКА:
Запустите setup_autostart.bat чтобы добавить приложение в автозагрузку.

ВЕРСИЯ: 1.0
ПЛАТФОРМА: Windows
ЛИЦЕНЗИЯ: MIT

Наслаждайтесь! 🚀
================================================================================
"""
    
    readme_path = dist_path / "README.txt"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"   ✅ Created: README.txt")
    
    # Step 7: Create archive
    print("\n📋 Step 7: Creating archive...")
    archive_path = repo_path / f"{dist_name}.zip"
    if archive_path.exists():
        archive_path.unlink()
    
    shutil.make_archive(
        str(repo_path / dist_name),
        "zip",
        dist_path.parent,
        dist_name
    )
    archive_size_mb = archive_path.stat().st_size / 1024 / 1024
    print(f"   ✅ Created: {dist_name}.zip ({archive_size_mb:.1f} MB)")
    
    # Summary
    print("\n" + "="*60)
    print("✅ BUILD SUCCESSFUL!")
    print("="*60)
    print(f"\n📁 Distribution folder: {dist_path}/")
    print(f"📦 Archive: {archive_path}")
    print(f"\nFiles included:")
    for file in dist_path.iterdir():
        if file.is_file():
            size = f"({file.stat().st_size / 1024:.0f} KB)" if file.stat().st_size < 1024*1024 else f"({file.stat().st_size / 1024 / 1024:.1f} MB)"
            print(f"  - {file.name} {size}")
    
    print(f"\n🚀 Ready to distribute!")
    print(f"   1. Share {dist_name}.zip or")
    print(f"   2. Copy files from {dist_name}/ folder")
    
    return True


def main():
    """Main entry point"""
    if not build_distribution():
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
