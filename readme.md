# 🎯 Keyboard Flipper Repository

Этот репозиторий содержит несколько утилит и приложений для работы с Ollama и текстовой обработкой.

## 📦 Проекты

### 1. 🎹 Keyboard Flipper (Конвертер раскладки)

**Портативное приложение для автоматического переключения раскладки клавиатуры.**

Забыли переключить раскладку? Просто нажмите `Ctrl+Shift+F` - приложение автоматически определит язык текста и переведёт его.

**Файлы:**
- `keyboard_flipper.py` - исходный код Python
- `dist/KeyboardFlipper.exe` - готовый к запуску EXE файл (6.7 MB, портативный)
- `run_keyboard_flipper.bat` - удобный запуск
- `keyboard_flipper_config.json` - конфигурация

**Документация:**
- [Подробное руководство](KEYBOARD_FLIPPER_USAGE.md)
- [Краткий README](KEYBOARD_FLIPPER_README.md)

**Быстрый старт:**
```bash
# Способ 1: Запустить готовый EXE
run_keyboard_flipper.bat

# Способ 2: Запустить Python скрипт
python keyboard_flipper.py
```

---

### 2. 🤖 Ollama Streamlit App

**Веб-интерфейс для работы с Ollama.**

```bash
streamlit run app.py
```

---

## 📋 Требования

- Windows 7+
- Python 3.7+ (для Python скриптов)
- Ollama (для Streamlit приложения)

---

## 🚀 Быстрый старт

### Keyboard Flipper (EXE)
```bash
run_keyboard_flipper.bat
```

### Keyboard Flipper (Python)
```bash
pip install keyboard pyperclip pystray pillow
python keyboard_flipper.py
```

### Streamlit App
```bash
pip install streamlit
streamlit run app.py
```

---

## 📝 Примечания

- **Keyboard Flipper** требует прав администратора для регистрации глобальных горячих клавиш
- Все приложения портативны - не требуют установки

---

## 📄 Лицензия

MIT


 & ".venv\Scripts\python.exe" keyboard_flipper.py
