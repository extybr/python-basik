""" Задача 1. Функции

Дана функция func_1, которая принимает число и возвращает
результат его сложения с числом 10: """


def func_2(function, *args):
    return function(*args) * 9


def func_1(num):
    return num + 10


number = int(input('number: '))
print(func_2(func_1, number))
