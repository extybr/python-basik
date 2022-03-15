import os
from typing import TextIO


class File:
    """ Класс файл менеджера """
    def __init__(self, name_file: str, mode: str) -> None:
        """
        Конструктор класса
        :param name_file: str
        :param mode: str
        """
        self.file = None
        self.name_file = name_file
        self.mode = mode

    def __enter__(self) -> TextIO:
        """
        Функция вводит контекст среды выполнения
        :return: TextIO
        """
        if not os.path.exists(self.name_file):
            self.file = open(self.name_file, 'w', encoding='utf-8')
        self.file = open(self.name_file, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        """
        Функция для выхода из контекста среды выполнения
        :param exc_type:
        :param exc_value:
        :param exc_traceback:
        :return: bool
        """
        self.file.close()
        return True


with File('text.txt', 'a') as my_file:
    my_file.write('Hello\n')
