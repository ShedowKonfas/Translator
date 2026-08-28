from deep_translator import GoogleTranslator

def translate_text(text, src_l, trgt_l):
    translator = GoogleTranslator(source=src_l.lower(), target=trgt_l.lower())
    return translator.translate(text)

if __name__ == '__main__':
    print("Translator | Переводчик")
    print("Выберите режим:")
    print("1. RU > EN")
    print("2. EN > RU")
    print("3. Свой язык > другой язык")
    print("0. Выход")

    choice = int(input("Ваш выбор: "))

    if choice == 0:
        quit()
    elif choice == 1:
        src_l, trgt_l = "ru", "en"
    elif choice == 2:
        src_l, trgt_l = "en", "ru"
    elif choice == 3:
        print("Пример кодов языков: en, ru, de, fr и т.д.")
        src_l = input("Первый язык (код): ").strip().lower()
        trgt_l = input("Второй язык (код): ").strip().lower()
    else:
        print("Неверный выбор")
        quit()

    text = input("Введите текст для перевода: ")
    result = translate_text(text, src_l, trgt_l)
    print("Перевод:", result)

