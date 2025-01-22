# Практическая работа 6
# Вариант 7

# Задание 2
# Переставить в одномерном массиве минимальный элемент и максимальный.

def swap_min_max(arr):
    if not arr:
        print("Массив пуст. Нечего переставлять.")
        return arr
    
    min_value = min(arr)
    max_value = max(arr)
    
    min_indices = [i for i, x in enumerate(arr) if x == min_value]
    max_indices = [i for i, x in enumerate(arr) if x == max_value]
    
    for i in min_indices:
        arr[i] = max_value
    for i in max_indices:
        arr[i] = min_value
    
    return arr

# Пример использования
input_array = list(map(int, input("Введите элементы массива через пробел: ").split()))
result_array = swap_min_max(input_array)
print("Обновленный массив:", result_array)
