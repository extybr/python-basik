""" Ищем файл с паролями """

import os


def find_password():
    for root, dirs, files in os.walk(r'F:\Games\steam'):
        for name in files:
            fullname = os.path.join(root, name)
            print(fullname)
            if 'pass.txt' in fullname:
                return print('Бинго!!!')


find_password()

