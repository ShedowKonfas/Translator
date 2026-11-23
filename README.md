# Translator

Консольный переводчик через `GoogleTranslator` из пакета `deep_translator`. За один запуск переводит один текст.

## Быстрый старт

```bat
pip install deep-translator
python main.py
```

`start.cmd` запускает то же через `py main.py`. `start.sh` активирует `venv/bin/activate` и выполняет `python3 main.py`.

## Меню

```
1. RU > EN
2. EN > RU
3. Свой язык > другой язык   (коды: en, ru, de, fr и т.д.)
0. Выход
```

## Пример

```bat
python main.py
```

```
Выберите режим:
1. RU > EN
2. EN > RU
3. Свой язык > другой язык
0. Выход
Ваш выбор: 1
Введите текст для перевода: Привет
Перевод: Hello
```

## Структура

- `main.py` — меню, выбор языков и вызов `GoogleTranslator`;
- `start.cmd`, `start.sh` — скрипты запуска;
- `README.md`, `AGENTS.md` — документация.

## Подводные камни

- Нужен доступ к интернету: перевод идёт через Google.
- `requirements.txt` и тесты отсутствуют. Не добавляйте тесты без запроса.
