""" Задача 3. Корень диска

Напишите программу, которая выводит на экран только корень
 диска, на котором запущен скрипт. Учтите, что скрипт может
 быть запущен где угодно и при любой вложенности папок.

Результат программы на примере диска G:
Корень диска: G:\\  """

import os


def print_dir(files):
    print(f'\nКорень диска: {files}')
    for item in os.listdir(files):
        path = os.path.join(files, item)
        print('    ', path)


folder_path = os.path.abspath(os.path.join('F:'))
print_dir(folder_path)