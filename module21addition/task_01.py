""" Задача 1. Challenge

Обычно программисты любят, когда всё просто и понятно.
 Но Антон не из таких. Он любит устраивать себе челлендж,
  развиваться и сразу применять на практике то, что только 
  что узнал. И в этот раз он подумал реализовать подсчёт 
  факториала без использования циклов.


Напишите функцию, которая считает факториал числа с помощью
 рекурсии.


Кстати, в Python есть ограничение на количество рекурсивных
 вызовов. Попробуйте передать своей функции, например, 
 число 1000 и посмотрите, что будет. """


import math


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


print(factorial(9), math.factorial(9))
