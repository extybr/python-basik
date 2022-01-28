""" Задача 3. Удаление части

#  Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу, которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков. """

import random

numbers = int(input('Кол-во чисел: '))
my = list(range(numbers))
print(my)

rand = [random.randint(1, 10) for _ in range(2)]
print(rand)

if rand[0] <= rand[1]:
    a, b = rand[0], rand[1]
    print(my[rand[0]:rand[1]])
else:
    a, b = rand[1], rand[0]
    print(my[rand[1]:rand[0]])
c, d = my[:a], my[b:]
c.extend(d)
print(c)
