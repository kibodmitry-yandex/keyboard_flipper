# 📑 KEYBOARD FLIPPER - ПОЛНЫЙ ИНДЕКС МАТЕРИАЛОВ

## 📦 Готовый дистрибутив (скопируйте эту папку)

```
KeyboardFlipper_Portable/
├── KeyboardFlipper.exe              (6.7 MB) ← ГЛАВНЫЙ ФАЙЛ
├── keyboard_flipper_config.json     (конфиг)
├── run_keyboard_flipper.bat         (запуск)
├── setup_autostart.bat              (автозагрузка)
└── README.txt                       (краткая инструкция)
```

**Или скачайте:** `KeyboardFlipper_Portable.zip` (6.6 MB)

---

## 📚 Документация

### 🚀 Для быстрого старта
- **[CHEATSHEET.md](CHEATSHEET.md)** - шпаргалка на одну страницу
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - полное руководство (для этого файла в дистрибутиве - README.txt)

### 📖 Для пользователей
- **[KEYBOARD_FLIPPER_README.md](KEYBOARD_FLIPPER_README.md)** - общее описание
- **[KEYBOARD_FLIPPER_USAGE.md](KEYBOARD_FLIPPER_USAGE.md)** - примеры использования и архитектура

### 👨‍💻 Для разработчиков
- **[keyboard_flipper.py](keyboard_flipper.py)** - исходный код приложения
- **[build_exe.py](build_exe.py)** - скрипт сборки EXE
- **[build_distribution.py](build_distribution.py)** - скрипт создания дистрибутива
- **[keyboard_flipper_config_tool.py](keyboard_flipper_config_tool.py)** - интерактивный конфигуратор

---

## 🎯 Где какой файл использовать?

### Для КОНЕЧНОГО ПОЛЬЗОВАТЕЛЯ

**Нужно:**
```
KeyboardFlipper_Portable/
├── KeyboardFlipper.exe          ← Запустить это
├── run_keyboard_flipper.bat     ← Или это
└── keyboard_flipper_config.json ← Отредактировать при необходимости
```

**Читать:** CHEATSHEET.md или README.txt (в папке)

---

### Для РАЗРАБОТЧИКА / МОДИФИКАЦИИ

**Нужно:**
```
G:\Ollama\repo\
├── keyboard_flipper.py          ← Отредактировать КОД
├── build_exe.py                 ← Пересобрать EXE
├── build_distribution.py        ← Создать новый дистрибутив
└── keyboard_flipper_config.json ← Конфиг по умолчанию
```

**Читать:** SETUP_GUIDE.md → раздел "Для разработчиков"

---

## 🔄 Рабочий процесс

### Новому пользователю

1. ✅ Скачать `KeyboardFlipper_Portable.zip`
2. ✅ Распаковать
3. ✅ Запустить `run_keyboard_flipper.bat`
4. ✅ Нажать `Ctrl+Shift+F` на выделенном тексте
5. ✅ (Опционально) Отредактировать `keyboard_flipper_config.json`
6. ✅ (Опционально) Запустить `setup_autostart.bat`

**Время на настройку:** 2 минуты

---

### Разработчику (для модификации)

1. ✅ Отредактировать `keyboard_flipper.py`
2. ✅ Установить зависимости: `pip install ...`
3. ✅ Запустить `python build_exe.py`
4. ✅ Протестировать `dist/KeyboardFlipper.exe`
5. ✅ Запустить `python build_distribution.py`
6. ✅ Распаковать и тестировать `KeyboardFlipper_Portable.zip`

**Время на изменение:** 5-10 минут

---

## 📊 Структура проекта

```
G:\Ollama\repo/                          (корневая папка)
│
├── 📄 Документация
│   ├── CHEATSHEET.md                   (шпаргалка - НАЧНИТЕ ОТСЮДА)
│   ├── SETUP_GUIDE.md                  (полное руководство)
│   ├── KEYBOARD_FLIPPER_README.md      (описание проекта)
│   ├── KEYBOARD_FLIPPER_USAGE.md       (примеры и архитектура)
│   ├── readme.md                       (основной README репо)
│   └── INDEX.md                        (этот файл)
│
├── 🐍 Python код
│   ├── keyboard_flipper.py             (ГЛАВНЫЙ КОД)
│   ├── keyboard_flipper_config_tool.py (конфигуратор)
│   ├── build_exe.py                    (сборка EXE)
│   └── build_distribution.py           (создание дистрибутива)
│
├── ⚙️ Конфигурация
│   └── keyboard_flipper_config.json    (конфиг по умолчанию)
│
├── 🖱️ Батники
│   ├── run_keyboard_flipper.bat        (запуск приложения)
│   └── setup_autostart.bat             (автозагрузка)
│
├── 📦 Скомпилированные
│   ├── dist/
│   │   └── KeyboardFlipper.exe         (скомпилированный EXE)
│   │
│   ├── KeyboardFlipper_Portable/       (готовый дистрибутив)
│   │   ├── KeyboardFlipper.exe
│   │   ├── keyboard_flipper_config.json
│   │   ├── run_keyboard_flipper.bat
│   │   ├── setup_autostart.bat
│   │   └── README.txt
│   │
│   └── KeyboardFlipper_Portable.zip    (архив для распространения)
│
└── 📝 Прочее
    ├── .instructions.md                (инструкции для рабочей среды)
    ├── .venv/                          (Python виртуальное окружение)
    ├── build/                          (временные файлы при сборке)
    └── KeyboardFlipper.spec            (конфиг PyInstaller)
```

---

## 🚀 Три способа запуска

### Способ 1️⃣: Готовый EXE (для конечного пользователя)

```bash
# Просто откройте:
KeyboardFlipper_Portable/KeyboardFlipper.exe
```

**Плюсы:** Ничего не надо устанавливать  
**Минусы:** Нельзя менять код

---

### Способ 2️⃣: Батник (для удобства)

```bash
# Откройте батник:
run_keyboard_flipper.bat
```

**Плюсы:** Удобный запуск, хорошие сообщения об ошибках  
**Минусы:** Нужна батка в папке

---

### Способ 3️⃣: Python скрипт (для разработки)

```bash
# Установите зависимости
pip install keyboard pyperclip pystray pillow

# Запустите
python keyboard_flipper.py
```

**Плюсы:** Легко менять и тестировать код  
**Минусы:** Нужна установка зависимостей

---

## 📋 Быстрые команды

### Установка

```bash
# Одной строкой установить всё
pip install keyboard pyperclip pystray pillow pyinstaller
```

### Разработка

```bash
# Запустить приложение (Python)
python keyboard_flipper.py

# Запустить конфигуратор
python keyboard_flipper_config_tool.py
```

### Сборка

```bash
# Собрать EXE
python build_exe.py

# Создать дистрибутив (всё в одну папку + ZIP)
python build_distribution.py
```

---

## ✅ Чек-лист для распространения

Перед тем как поделиться приложением:

- [ ] Протестирован EXE файл
- [ ] Протестирована горячая клавиша
- [ ] Работает перевод РУ↔EN раскладки
- [ ] Работает батник запуска
- [ ] Работает автозагрузка
- [ ] Конфиг легко редактировать
- [ ] Документация понятна
- [ ] ZIP архив создан
- [ ] ZIP архив протестирован на другом ПК

---

## 🔗 Навигация

| Раздел | Файл |
|--------|------|
| 📍 **Начните отсюда** | [CHEATSHEET.md](CHEATSHEET.md) |
| 🚀 **Полное руководство** | [SETUP_GUIDE.md](SETUP_GUIDE.md) |
| 💻 **Для разработчиков** | [SETUP_GUIDE.md#для-разработчиков](SETUP_GUIDE.md#для-разработчиков) |
| 🎹 **Что это?** | [KEYBOARD_FLIPPER_README.md](KEYBOARD_FLIPPER_README.md) |
| 📖 **Примеры использования** | [KEYBOARD_FLIPPER_USAGE.md](KEYBOARD_FLIPPER_USAGE.md) |
| 📦 **Скачать** | [KeyboardFlipper_Portable.zip](KeyboardFlipper_Portable.zip) |

---

## 💾 Размеры файлов

| Файл | Размер | Назначение |
|------|--------|-----------|
| KeyboardFlipper.exe | 6.7 MB | Основное приложение |
| KeyboardFlipper_Portable.zip | 6.6 MB | Архив для распространения |
| keyboard_flipper.py | ~10 KB | Исходный код |
| Документация (все .md) | ~150 KB | Руководства и примеры |

---

## 📞 Поддержка

### Ошибка: "Горячая клавиша не работает"

✅ Решение:
1. Запустите приложение от администратора
2. Проверьте config.json синтаксис
3. Попробуйте другую комбинацию клавиш

### Ошибка: "KeyboardFlipper.exe не найден"

✅ Решение:
1. Убедитесь, что `dist/KeyboardFlipper.exe` существует
2. Пересоберите: `python build_exe.py`

### Вопрос: "Как добавить свою раскладку?"

✅ Решение: Отредактируйте `keyboard_flipper.py`:
- Найдите `LAYOUTS = {`
- Добавьте новую раскладку
- Пересоберите EXE

---

## 📄 История версий

| Версия | Дата | Что изменилось |
|--------|------|----------------|
| 1.0 | 15.07.2026 | Первый релиз |

---

## 🎓 Образовательная ценность

Этот проект демонстрирует:
- ✅ Глобальные горячие клавиши в Python
- ✅ Работа с буфером обмена
- ✅ Системный трей приложения
- ✅ JSON конфигурация
- ✅ PyInstaller сборка в EXE
- ✅ Распределение Python приложений

**Идеально для обучения:**
- Начинающим Python разработчикам
- Для проектов на курсах программирования
- Для портфолио на собеседование

---

## 📜 Лицензия

**MIT License** - полная свобода использования, модификации и распространения

---

**Keyboard Flipper v1.0**  
Автоматический конвертер раскладки клавиатуры  
Портативное, стендалон приложение для Windows  

Создано: 15.07.2026
