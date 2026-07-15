"""
Keyboard Flipper - minimal clipboard-only layout flipper
Behavior: on hotkey, read clipboard, flip keyboard layout (ru<->us), write back to clipboard.
"""

import json
import logging
import threading
import time
import os
from pathlib import Path
import sys

import keyboard
import pyperclip
from PIL import Image, ImageDraw
import pystray


DEFAULT_CONFIG = {
    "hotkey": "ctrl+alt+f",
    "keyboard_layout": "ru_us",
    "debounce_ms": 300,
    "enable_log": False,
    "mapping": {
        "ё": "`", "й": "q", "ц": "w", "у": "e", "к": "r", "е": "t", "н": "y",
        "г": "u", "ш": "i", "щ": "o", "з": "p", "х": "[", "ъ": "]",
        "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h",
        "о": "j", "л": "k", "д": "l", "ж": ";", "э": "'",
        "я": "z", "ч": "x", "с": "c", "м": "v", "и": "b", "т": "n", "ь": "m",
        "б": ",", "ю": ".", "&": "?", "/": ".", "?": ",",
        "Ё": "~", "Й": "Q", "Ц": "W", "У": "E", "К": "R", "Е": "T", "Н": "Y",
        "Г": "U", "Ш": "I", "Щ": "O", "З": "P", "Х": "{", "Ъ": "}",
        "Ф": "A", "Ы": "S", "В": "D", "А": "F", "П": "G", "Р": "H",
        "О": "J", "Л": "K", "Д": "L", "Ж": ":", "Э": '"',
        "Я": "Z", "Ч": "X", "С": "C", "М": "V", "И": "B", "Т": "N", "Ь": "M",
        "Б": "<", "Ю": ">",
        # mapping from Russian char to US char; reverse is computed automatically
        # ensure '.' is produced by 'ю' in ru->us mapping so reverse maps '.' -> 'ю'
    }
}


class LayoutFlipper:
    @staticmethod
    def count_layout(text: str):
        cyr = sum(1 for c in text if '\u0400' <= c <= '\u04FF')
        lat = sum(1 for c in text if c.isascii() and c.isalpha())
        return cyr, lat

    @staticmethod
    def flip_text(text: str, forward_map: dict, reverse_map: dict) -> str:
        cyr, lat = LayoutFlipper.count_layout(text)
        mapping = reverse_map if lat > cyr else forward_map
        return ''.join(mapping.get(ch, ch) for ch in text)


class Config:
    def __init__(self, path: Path):
        self.path = path
        self.hotkey = DEFAULT_CONFIG["hotkey"]
        self.keyboard_layout = DEFAULT_CONFIG["keyboard_layout"]
        self.debounce_ms = DEFAULT_CONFIG.get("debounce_ms", 300)
        self.mapping = DEFAULT_CONFIG["mapping"].copy()
        self.mtime = 0
        self.ensure()
        self.load()

    def ensure(self):
        if not self.path.exists():
            try:
                self.path.write_text(json.dumps(DEFAULT_CONFIG, ensure_ascii=False, indent=2), encoding='utf-8')
            except Exception:
                pass

    def load(self):
        try:
            # If config missing, recreate from defaults
            if not self.path.exists():
                logging.info('Config missing on disk — recreating default config')
                self.ensure()
                try:
                    self.mtime = self.path.stat().st_mtime
                except Exception:
                    self.mtime = 0
                self.mapping = DEFAULT_CONFIG["mapping"].copy()
                self.hotkey = DEFAULT_CONFIG["hotkey"]
                self.keyboard_layout = DEFAULT_CONFIG["keyboard_layout"]
                return True

            m = self.path.stat().st_mtime
            if m == self.mtime:
                return False
            self.mtime = m
            data = json.loads(self.path.read_text(encoding='utf-8'))
            self.hotkey = data.get('hotkey', self.hotkey)
            self.keyboard_layout = data.get('keyboard_layout', self.keyboard_layout)
            self.debounce_ms = data.get('debounce_ms', self.debounce_ms)
            mapping = data.get('mapping')
            if isinstance(mapping, dict):
                self.mapping = mapping
            return True
        except Exception:
            logging.exception('Failed loading config')
        return False


class KeyboardFlipperApp:
    def __init__(self, config_path: Path):
        # Delay logging setup until config is loaded so `enable_log` controls file logging
        self.config_path = config_path
        self.config = Config(config_path)
        self.setup_logging()
        self.flipper = LayoutFlipper()
        self.hotkey_handler = None
        self.last_trigger = 0.0
        self.stop_event = threading.Event()
        self.icon = None
        logging.info('Keyboard Flipper initialized')

    def setup_logging(self):
        # Remove existing handlers
        for h in list(logging.root.handlers):
            logging.root.removeHandler(h)
        handlers: list[logging.Handler] = [logging.StreamHandler()]
        try:
            if getattr(self.config, 'enable_log', False):
                log_path = Path(self.config.path).parent / 'keyboard_flipper.log'
                fh = logging.FileHandler(str(log_path), encoding='utf-8')
                handlers.insert(0, fh)
        except Exception:
            pass
        logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', handlers=handlers)

    def ensure_icon_files(self):
        # Do not write icon files to disk at runtime. If an icon PNG exists
        # next to the executable/script, load it. Otherwise create an in-memory
        # placeholder image for the tray; do not save any files.
        if getattr(sys, 'frozen', False):
            base = Path(sys.argv[0]).resolve().parent
        else:
            base = Path(__file__).parent
        png = base / 'icon.png'
        try:
            if png.exists():
                img = Image.open(png).convert('RGBA')
            else:
                img = Image.new('RGBA', (64, 64), (0, 122, 204, 255))
                d = ImageDraw.Draw(img)
                d.text((12, 18), 'KF', fill='white')
        except Exception:
            img = Image.new('RGBA', (64, 64), (0, 122, 204, 255))
        # Return only an Image object; no disk operations
        return img, None

    def open_settings(self, icon=None, item=None):
        try:
            os.startfile(self.config_path)
        except Exception:
            logging.exception('Failed to open settings')

    def exit_app(self, icon=None, item=None):
        logging.info('Exit requested')
        self.stop_event.set()
        try:
            if self.icon:
                self.icon.stop()
        except Exception:
            pass
        keyboard.unhook_all_hotkeys()

    def apply_hotkey(self):
        try:
            if self.hotkey_handler:
                try:
                    keyboard.remove_hotkey(self.hotkey_handler)
                except Exception:
                    pass
            self.hotkey_handler = keyboard.add_hotkey(self.config.hotkey, lambda: threading.Thread(target=self.on_hotkey).start())
            logging.info(f"Registered hotkey: {self.config.hotkey}")
        except Exception:
            logging.exception('Failed to register hotkey')

    def on_hotkey(self):
        try:
            now = time.time() * 1000.0
            if now - self.last_trigger < (self.config.debounce_ms or 0):
                logging.info('Hotkey ignored due to debounce')
                return
            self.last_trigger = now
            logging.info('Hotkey pressed: flipping clipboard')
            text = pyperclip.paste()
            if not text:
                logging.info('Clipboard empty — nothing to flip')
                return
            forward = self.config.mapping
            reverse = {v: k for k, v in forward.items()}
            flipped = self.flipper.flip_text(text, forward, reverse)
            if flipped != text:
                pyperclip.copy(flipped)
                logging.info(f"Clipboard flipped: '{text[:60]}' -> '{flipped[:60]}'")
            else:
                logging.info('Clipboard does not need conversion')
        except Exception:
            logging.exception('Error in hotkey handler')

    def run_tray(self):
        image, _ = self.ensure_icon_files()
        menu = pystray.Menu(pystray.MenuItem('Open settings', lambda icon, item: self.open_settings(icon, item)), pystray.MenuItem('Exit', lambda icon, item: self.exit_app(icon, item)))
        self.icon = pystray.Icon('keyboard_flipper', image, 'Keyboard Flipper', menu)
        self.icon.run()

    def run(self):
        # initial hotkey
        self.apply_hotkey()

        # start tray in separate thread
        t = threading.Thread(target=self.run_tray, daemon=True)
        t.start()

        try:
            while not self.stop_event.is_set():
                changed = self.config.load()
                if changed:
                    logging.info('Config changed on disk — applying')
                    self.apply_hotkey()
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info('Exiting')
        finally:
            try:
                if self.icon:
                    self.icon.stop()
            except Exception:
                pass


if __name__ == '__main__':
    # Choose config path: when frozen by PyInstaller, place sidecar next to the executable.
    if getattr(sys, 'frozen', False):
        # For onefile executables, sys.argv[0] points to the original exe location; use that so config stays next to exe
        base_dir = Path(sys.argv[0]).resolve().parent
    else:
        base_dir = Path(__file__).parent
    cfg = base_dir / 'keyboard_flipper_config.json'
    app = KeyboardFlipperApp(cfg)
    app.run()
