""" Задача 2. Содержимое

Выберите любую директорию на своём диске и затем напишите программу, 
выводящую на экран абсолютные пути к файлам и папкам, которые находятся
внутри этой директории.  """

import os


def print_dir(files):
    print(f'\nСодержимое папки {files}')
    for item in os.listdir(files):
        path = os.path.join(files, item)
        print('    ', path)


folder_lst = list()
number = int(input('Кол-во папок для поиска: '))
for i in range(number):
    folder_name = input('Введите название папки: ')
    folder_lst.append(folder_name)
for folder in folder_lst:
    folder_path = os.path.abspath(os.path.join('I:/0000000/Telegram Desktop', folder))
    # folder_path = os.path.abspath(os.path.join('..', '..', folder))
    print_dir(folder_path)