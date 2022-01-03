""" Задача 1. Результаты

Одному программисту дали задачу для обработки неких результатов 
тестирования двух групп людей. Файл первой группы (group_1.txt) 
находится в папке task, файл второй группы (group_2.txt) — в 
папке Additional_info. """

import os

file = open(os.path.join('C:/', 'task', 'group_1.txt'), 'r', encoding='UTF-8')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])

file = open(os.path.join('C:/', 'task', 'group_1.txt'), 'r', encoding='UTF-8')
diff = 0
for i_line in file:
    info = i_line.split()
    diff = abs(diff - int(info[2]))

file_2 = open(os.path.join('C:\\', 'task', 'Additional_info', 'group_2.txt'), 'r', encoding='UTF-8')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

print(summa)
print(diff)
print(compose)
