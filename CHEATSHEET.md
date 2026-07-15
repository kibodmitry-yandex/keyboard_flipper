# 📝 KEYBOARD FLIPPER - ШПАРГАЛКА

## ⚡ Ультра-быстрый старт

```
1. Запустить:           run_keyboard_flipper.bat
2. Горячая клавиша:     Ctrl+Shift+F
3. Выделить текст:      Ctrl+A или мышью
4. Нажать:              Ctrl+Shift+F → готово! ✨
```

---

## 📂 Важные файлы

| Файл | Что это |
|------|---------|
| `KeyboardFlipper.exe` | **ГЛАВНЫЙ** - запускайте его |
| `keyboard_flipper_config.json` | Конфигурация (горячая клавиша) |
| `run_keyboard_flipper.bat` | Удобный запуск |
| `keyboard_flipper.py` | Python код (если хотите редактировать) |

---

## 🎹 Горячие клавиши (в config.json)

```json
{
  "hotkey": "ctrl+shift+f",          ← ИЗМЕНИТЕ ЗДЕСЬ
  "keyboard_layout": "ru_us"
}
```

### Примеры замены:

- `"hotkey": "alt+z"`                 ← Alt+Z вместо Ctrl+Shift+F
- `"hotkey": "f12"`                  ← Просто F12
- `"hotkey": "ctrl+alt+x"`           ← Ctrl+Alt+X
- `"hotkey": "win+k"`                ← Windows+K

---

## 💻 Команды (для разработчиков)

```bash
# Запустить Python скрипт
python keyboard_flipper.py

# Запустить конфигуратор
python keyboard_flipper_config_tool.py

# Пересобрать EXE (нужен PyInstaller)
python build_exe.py

# Создать дистрибутив (всё в одной папке)
python build_distribution.py
```

---

## 🔧 Установка зависимостей

```bash
pip install keyboard pyperclip pystray pillow pyinstaller
```

---

## 📊 Статус

| Компонент | Статус |
|-----------|--------|
| EXE (готовый) | ✅ Работает |
| Config | ✅ Работает |
| Автозагрузка | ✅ Работает |
| Горячая клавиша | ✅ Работает |
| Конвертер раскладки | ✅ Работает (РУ↔EN) |

---

## 🆘 Частые проблемы

| Проблема | Решение |
|----------|---------|
| Горячая клавиша не работает | Запустите от администратора |
| Config не загружается | Проверьте JSON синтаксис |
| Текст не переворачивается | Выделите текст перед нажатием горячей клавиши |
| Приложение падает | Проверьте комбинацию клавиш в config.json |

---

## 📌 Примеры использования

### Браузер

```
Написали:   gthbdtn! Rfr gjvf ,hjn?
Выделили:   это всё
Ctrl+Shift+F
Результат:  Привет! Как дома вроде?
```

### Photoshop

```
Текстовый слой → Ctrl+A → Ctrl+Shift+F → готово!
```

### VSCode комментарий

```python
# Написали:  d ,jkmirf,jcnb
# Выделили это
# Ctrl+Shift+F
# Результат: в большабости
```

---

## 🎯 Что дальше?

- ✅ Версия готова к использованию
- ✅ Портативна - не требует установки
- ✅ Настраивается через JSON
- 📋 Можно расширить на другие раскладки
- 📋 Можно добавить GUI настройки

---

## 📦 Распространение

```bash
# Готовый пакет в:
KeyboardFlipper_Portable.zip
```

Содержит:
- ✅ KeyboardFlipper.exe
- ✅ keyboard_flipper_config.json
- ✅ run_keyboard_flipper.bat
- ✅ setup_autostart.bat
- ✅ README.txt

---

## 🔒 Безопасность

- ✅ Никаких сетевых подключений
- ✅ Никаких данных не передаются
- ✅ Работает полностью локально
- ✅ Open source (можете проверить код)

---

**v1.0** | Keyboard Flipper | MIT License

