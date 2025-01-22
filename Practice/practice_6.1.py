# Практическая работа 6
# Вариант 7

# Задание 1
# Дан массив целых чисел. Найти сумму элементов с четными номерами и произведение элементов с нечетными номерами. Вывести сумму и произведение.

def process_array(arr):
    even_sum = 0
    odd_product = 1
    
    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum += arr[i]
        else:
            odd_product *= arr[i]
    
    return even_sum, odd_product

# Пример использования
input_array = list(map(int, input("Введите элементы массива через пробел: ").split()))
even_sum, odd_product = process_array(input_array)
print(f"Сумма элементов с чётными номерами: {even_sum}")
print(f"Произведение элементов с нечётными номерами: {odd_product}")