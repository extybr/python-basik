print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

point_a = int(input('Введите первое число: '))
point_b = int(input('Введите второе число: '))
summa = 0
count = 0
for number in range(point_a, point_b + 1):
    if number % 3 == 0:
        summa += number
        count += 1
middle = summa / count
print('Среднее арифметическое всех чисел из отрезка: ', middle)
