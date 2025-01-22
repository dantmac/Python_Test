# Задание 7

# По данному натуральному числу n вычислите сумму 1! +2! +3!+... +n!. В решении этой задачи можно использовать только один цикл. 
# Пользоваться математической библиотекой math в этой задаче запрещено.

def sum_of_factorials(n):
    if n <= 0:
        return "Ошибка: вводимое число НЕ должно быть меньше 1!"
    
    factorial = 1
    total_sum = 0
    
    for i in range(1, n + 1):
        factorial *= i
        total_sum += factorial
    return total_sum

# Пример использования
number_n = int(input("Введите натуральное число: "))
print("Сумма факториалов:", sum_of_factorials(number_n))