""" Задача 2. Словари из списков

Создайте два списка, в каждом из которых лежит 10
случайных букв алфавита (могут повторяться). 
Затем для каждого списка создайте словарь из пар
«индекс — значение» и выведите оба словаря на экран. """

import random
alphabet = tuple('abcdefghijklmnopqrstuvwxyz')
print(alphabet)
first = [random.choice(alphabet) for _ in range(10)]
second = [random.choice(alphabet) for _ in range(10)]
print(first, second)
new = dict()
for a, b in enumerate(first):
    ab = {a: b}
    new.update(ab)
print(new)

