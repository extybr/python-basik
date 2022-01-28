
import random

stick = int(input('Кол-во палок: '))
throw = int(input('Кол-во бросков: '))
skittles = ['I'] * stick
for run in range(throw):
    left, right = [random.randint(1, 10), random.randint(1, 10)]
    if left > right:
        right, left = left, right
    skittles[left - 1:right] = ['.'] * (right - left + 1)
    print(f'Бросок {run + 1}. Сбиты палки с номера {left}\nпо номер {right}')
result = ''
for index in skittles:
    result += index
print(f'\nРезультат: {result}', end=' ')

# зачет!
