# Практическая работа 9
# Вариант 7

# Задание 2
# Для заданной квадратной матрицы сформировать одномерный массив из ее диагональных элементов.
# Найти след матрицы, просуммировав элементы одномерного массива.
# Преобразовать исходную матрицу по правилу: четные строки разделить на полученное значение, нечетные оставить без изменения.
# P.S. Организовать ввод из файла и вывод данных в файл.

with open('Practice/vvod.txt', 'r') as infile:
    matrix = [list(map(int, line.split())) for line in infile.readlines()]

n = len(matrix)

for i, row in enumerate(matrix):
    if len(row) != n:
        raise ValueError(f"Ошибка: строка {i+1} имеет неверное количество элементов. Ожидается {n}, но получено {len(row)}.")

diag = sum(matrix, [])[::len(matrix) + 1]
trace = sum(diag)

for i in range(0, len(matrix), 2):  # Для четных строк (по индексу)
    matrix[i] = [v / trace for v in matrix[i]]

with open('Practice/vivod.txt', 'w') as outfile:
    for row in matrix:
        outfile.write(" ".join(map(str, row)) + '\n')

print("Матрица была успешно преобразована и сохранена в vivod.txt.")