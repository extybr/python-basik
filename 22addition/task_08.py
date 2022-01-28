""" Задача 1. Сумма чисел

Во входном файле numbers.txt записано N целых чисел, каждое
в отдельной строке. Напишите программу, которая выводит их
сумму в выходной файл answer.txt. """

file = open('numbers.txt', 'r', encoding='utf-8')

new = open('new.txt', 'a')
summa = 0
for i in file:
    summa += int(i)
new.write(str(summa))
new.write('\n')
file.close()
new_read = open('new.txt', 'r')
for j in new_read:
    print(j, end='')
new.close()