""" # Задача 2. Соседи

# Дана строка S и номер позиции символа в строке. Напишите программу, которая выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей: их нет, есть ровно один или есть два таких же. 

Пример 1:
Введите строку: abbc
Номер символа: 3
Символ слева: b
Символ справа: c
Есть ровно один такой же символ. """

text = input('Введите строку: ')
number = int(input('Номер символа: '))
count = -1
for i in text:
    if text[number - 1] == i:
        count += 1

left = text[number - 2]
right = text[number]
print(f'Символ слева: {left}')
print(f'Символ справа: {right}')
if count > 0:
    print(f'Есть еще {count} таких символа(ов).')
else:
    print('Таких же символов нет.')