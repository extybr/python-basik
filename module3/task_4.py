print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

side_a = int(input('Введите длину первого катета: '))
side_b = int(input('Введите длину второго катета: '))
square = side_a * side_b / 2
print('Площадь треугольника равна: ', square)