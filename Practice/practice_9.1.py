# Практическая работа 9
# Вариант 7

# Задание 1
# Квадратная матрица, симметричная относительно главной диагонали, задана верхним треугольником в виде одномерного массива.
# Восстановить исходную матрицу и напечатать по строкам.

with open('Practice/vvod.txt', 'r') as infile:
    matrix_data = list(map(int, infile.read().split()))

n = int((2 * len(matrix_data)) ** 0.5)

expected_elements = n * (n + 1) // 2
if len(matrix_data) != expected_elements:
    raise ValueError(f"Ошибка: количество элементов в файле не соответствует верхнему треугольнику матрицы. Ожидается {expected_elements}, но получено {len(matrix_data)}.")

matr = [[0 for _ in range(n)] for _ in range(n)]

index = 0
for i in range(n):
    matr[i][i] = matrix_data[index]
    index += 1
    for j in range(i + 1, n):
        matr[i][j] = matrix_data[index]
        matr[j][i] = matr[i][j]
        index += 1

with open('Practice/vivod.txt', 'w') as outfile:
    for row in matr:
        outfile.write(" ".join(map(str, row)) + '\n')

print("Матрица была успешно восстановлена и сохранена в vivod.txt.")