# Практическая работа 7
# Вариант 7

# Задание 1
# Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его площадь, если угол между сторонами длиной X и У — прямой. 
# Использовать две подпрограммы для вычисления площадей: прямоугольного треугольника и прямоугольника.

import math

def right_triangle_area(X, Y):
    return 0.5 * X * Y

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

area_1 = right_triangle_area(X, Y)
hypotenuse = math.sqrt(X**2 + Y**2)
area_2 = triangle_area(hypotenuse, Z, T)
total_area = area_1 + area_2

print(f"Площадь четырехугольника: {total_area}")