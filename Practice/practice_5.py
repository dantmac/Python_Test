# Практическая работа 5
# Вариант 7

def replace_p_with_stars(s):
    if not isinstance(s, str):
        raise ValueError("Ошибка: Ввод должен быть строкой")
    
    length = len(s)
    half_length = length // 2
    first_half = s[:half_length]
    second_half = s[half_length:]
    
    first_half_modified = first_half.replace("п", "*")
    result = first_half_modified + second_half

    return result

# Пример использования
try:
    input_value = input("Введите строку: ")
    output_string = replace_p_with_stars(input_value)
    print("Результат:", output_string)
except ValueError as e:
    print(e)