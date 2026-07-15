"""
Advanced configuration utility for Keyboard Flipper
Provides interactive setup and configuration
"""

import json
from pathlib import Path
import sys


def show_menu():
    """Show main configuration menu"""
    print("\n" + "="*50)
    print("⚙️  Keyboard Flipper - Configuration")
    print("="*50 + "\n")
    print("1️⃣  Изменить горячую клавишу")
    print("2️⃣  Изменить тип клавиатуры")
    print("3️⃣  Посмотреть текущие настройки")
    print("4️⃣  Восстановить настройки по умолчанию")
    print("5️⃣  Выход")
    print()


def load_config(config_path):
    """Load configuration from file"""
    if config_path.exists():
        try:
            return json.loads(config_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"❌ Ошибка при загрузке конфига: {e}")
            return None
    return None


def save_config(config_path, config):
    """Save configuration to file"""
    try:
        config_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"✅ Конфиг сохранён: {config_path}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
        return False


def show_hotkey_examples():
    """Show examples of valid hotkeys"""
    print("\n📋 Примеры горячих клавиш:")
    print("   ctrl+shift+f    (по умолчанию)")
    print("   alt+shift+x")
    print("   ctrl+alt+f")
    print("   f12")
    print("   shift+f12")
    print("   ctrl+shift+space")
    print("   win+k")
    print("\n💡 Формат: модификаторы + клавиша")
    print("   Модификаторы: ctrl, alt, shift, win")
    print("   Разделитель: +")


def change_hotkey(config):
    """Change hotkey in configuration"""
    print("\n🎹 Изменить горячую клавишу")
    print("-" * 40)
    show_hotkey_examples()
    
    hotkey = input("\nВведите новую горячую клавишу: ").strip()
    
    if not hotkey:
        print("❌ Горячая клавиша не может быть пустой")
        return False
    
    config["hotkey"] = hotkey
    print(f"✅ Горячая клавиша изменена на: {hotkey}")
    return True


def change_layout(config):
    """Change keyboard layout"""
    print("\n⌨️  Изменить тип клавиатуры")
    print("-" * 40)
    print("1️⃣  ru_us (Русский ↔ Английский, ЙЦУКЕН)")
    # Future: add more layouts
    print("\nДругие раскладки можно добавить в code")
    
    choice = input("\nВыберите раскладку (номер или введите вручную): ").strip()
    
    if choice == "1":
        layout = "ru_us"
    else:
        layout = choice
    
    if not layout:
        print("❌ Раскладка не может быть пустой")
        return False
    
    config["keyboard_layout"] = layout
    print(f"✅ Раскладка изменена на: {layout}")
    return True


def show_config(config):
    """Display current configuration"""
    print("\n📖 Текущие настройки:")
    print("-" * 40)
    print(f"Горячая клавиша:  {config.get('hotkey', 'N/A')}")
    print(f"Тип клавиатуры:   {config.get('keyboard_layout', 'N/A')}")


def reset_config():
    """Reset to default configuration"""
    return {
        "hotkey": "ctrl+shift+f",
        "keyboard_layout": "ru_us"
    }


def main():
    """Main configuration interface"""
    config_path = Path(__file__).parent / "keyboard_flipper_config.json"
    
    print("\n🔧 Keyboard Flipper - Конфигуратор")
    print("=" * 50)
    
    # Load existing config
    config = load_config(config_path)
    if config is None:
        print("⚠️  Конфиг не найден, используются настройки по умолчанию")
        config = reset_config()
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            if change_hotkey(config):
                if save_config(config_path, config):
                    print("✅ Изменения сохранены")
                    print("   Перезагрузите приложение для применения")
        
        elif choice == "2":
            if change_layout(config):
                if save_config(config_path, config):
                    print("✅ Изменения сохранены")
                    print("   Перезагрузите приложение для применения")
        
        elif choice == "3":
            show_config(config)
        
        elif choice == "4":
            confirm = input("\n⚠️  Восстановить настройки по умолчанию? (y/n): ").strip().lower()
            if confirm == "y":
                config = reset_config()
                if save_config(config_path, config):
                    print("✅ Настройки восстановлены")
            else:
                print("❌ Отменено")
        
        elif choice == "5":
            print("\n👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Пожалуйста, выберите 1-5")
        
        input("\n[Нажмите Enter для продолжения...]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
