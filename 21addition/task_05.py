""" Задача 2. Непонятно!

Друг никак не может понять эту тему с изменяемыми и неизменяемыми
типами, ссылками, объектами и их id. Видя, как он мучается, вы
решили добить помочь ему и объяснить эту тему наглядно.

Пользователь вводит любой объект. Напишите программу, которая 
выводит на экран тип введённых данных, информацию о его изменяемости,
а также id этого объекта. """

def f(data):
    if isinstance(data, int):
        print(f'Тип данных: int (целое число)\nНеизменяемый (immutable)\nId объекта: {id(data)}')
    elif isinstance(data, dict):
        print(f'Тип данных: dict (словарь)\nИзменяемый (mutable)\nId объекта: {id(data)}')
    elif isinstance(data, str):
        print(f'Тип данных: str (строка)\nНеизменяемый (immutable)\nId объекта: {id(data)}')


choice = {'Jack': 95715}
f(choice)
