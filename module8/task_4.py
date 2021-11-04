print('Задача 4. Отрезок')

#Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))
number_c = int(input('Введите число кратности: '))
count = 0
sum_number = 0
for number in range(number_a, number_b + 1):
    if number % number_c == 0:
        sum_number += number
        count += 1
middle = sum_number // count
print('Среднее арифметическое всех чисел из отрезка, кратные числу ', number_c, 'равны: ', middle)
