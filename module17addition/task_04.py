""" Задача 1. Список чётных чисел

#  Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B. Используйте list comprehensions (как и в следующих задачах). """

start = int(input('Введите первое число: '))
stop = int(input('Введите второе число: '))
odd = [i for i in range(start, stop + 1) if i % 2 == 0]
print(odd)