""" Задача 2. Сообщение

# Илья решил безобидно подшутить над другом и написал программу для смартфона, которая при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному добавляет ещё один дополнительный.

# Пользователь вводит строку и дополнительный символ. Напишите программу, которая генерирует два списка: в первом списке каждый элемент — удвоенная буква первой строки, во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа. """

my = list(input('Введите строку: '))
my_symbol = input('Введите дополнительный символ: ')
duble = [i * 2 for i in my]
my_duble = [i + my_symbol for i in duble]
print(f'Список удвоенных символов: {duble}')
print(f'Склейка с дополнительным символом: {my_duble}')
