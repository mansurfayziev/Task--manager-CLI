"""Функции безопасного ввода данных"""

def get_integer_input(prompt: str, min_value: int = None, max_value: int = None) -> int | None:
    """
    Запрос целого числа с валидацией.
    
    Args:
        prompt (str): Текст запроса.
        min_value (int, optional): Минимальное значение.
        max_value (int, optional): Максимальное значение.
    
    Returns:
        int | None: Введённое число или None (при пустом вводе).
    
    Examples:
        >>> get_integer_input("ID: ", min_value=1)
        ID: abc
        ❌ Ошибка: введите целое число
        ID: 0
        ❌ Ошибка: значение должно быть >= 1
        ID: 5
        5
    """
    # так как я еще не изучал try/except по этому без него делаю

    for x in range(3):
        inp = input(prompt).strip() 

        if inp=='':
            return None
        
        if not inp.isnumeric():
            print("❌ Ошибка: введите целое число")
            continue
        
        inp = int(inp)
        
        if max_value:
                if max_value < inp:
                    print(f"❌ Ошибка: значение должно быть <= {max_value}")
                    continue
        
        if min_value:
                if min_value > inp:
                    print(f"❌ Ошибка: значение должно быть >= {min_value}")
                    continue
    
        return inp
        


def get_string_input(prompt: str, allow_empty: bool = False) -> str | None:
    """
    Запрос строки с валидацией.
    
    Args:
        prompt (str): Текст запроса.
        allow_empty (bool): Разрешить пустую строку.
    
    Returns:
        str | None: Введённая строка или None.
    """

    for x in range(3):
        inp = input(prompt).strip()

        if allow_empty == False and inp == '':
            print("❌ Ошибка: поле не может быть пустым") 
            continue

        if inp == '':
            return None
        
        return inp


def get_choice_input(prompt: str, valid_choices: tuple) -> str | None:
    """
    Запрос выбора из списка.
    
    Args:
        prompt (str): Текст запроса.
        valid_choices (tuple): Допустимые значения.
    
    Returns:
        str | None: Выбранное значение или None.
    
    Examples:
        >>> get_choice_input("Приоритет: ", ("low", "medium", "high"))
        Приоритет: urgent
        ❌ Ошибка: выберите из: low, medium, high
        Приоритет: high
        'high'
    """
    # Case-insensitive (.lower())
    # Вывод списка допустимых значений при ошибке
    # Пустой ввод → None
    # Максимум 3 попытки

def confirm_action(message: str) -> bool:
    """
    Запрос подтверждения действия.
    
    Args:
        message (str): Текст сообщения.
    
    Returns:
        bool: True (y/yes), False (n/no/пустой ввод).
    """
    while True:
        inp = input(message).strip()
        inp = inp.lower()
        if inp == 'y' or inp == 'yes':
            return True
        if inp == 'n' or inp == 'no' or inp == '';
            return False