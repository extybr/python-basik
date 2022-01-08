""" Задача 1. Простая программа

Напишите программу, которая открывает файл и записывает туда введённую
пользователем строку. Используйте операторы try except else finally. 
Обработайте возможные ошибки:

    Проблема при открытии файла.
    Нельзя преобразовать данные в целое.
    Неожиданная ошибка. """


my_text = input('Введите строку: ')
text = open('text.txt', 'w', encoding='utf-8')
try:
    text.write(str(my_text))
    text.close()
    text = open('text.txt', 'r', encoding='utf-8')
    for line in text:
        print(int(line))
except FileNotFoundError:
    print('файл или директория не существует')
except PermissionError:
    print('не хватает прав доступа')
except ValueError:
    print('функция получает аргумент правильного типа, но некорректного значения')
finally:
    text.close()
	