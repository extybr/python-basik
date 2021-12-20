
import random

original = list(random.randint(0, 20) for _ in range(10))
print(f'Оригинальный список: {original}')

# вариант первый
right, left = [], []
for index in range(len(original)):
    if index % 2 == 0:
        right.append(original[index])
    elif index % 2 != 0:
        left.append(original[index])
doubles = list(tuple(zip(right, left)))
print(f'Новый список: {doubles}')

# /--> вариант второй <--\
right_second = [second for first, second in enumerate(original) if first % 2 == 0]
left_second = [second for first, second in enumerate(original) if first % 2 != 0]
doubles_second = list(tuple(zip(right_second, left_second)))
print(f'Новый 2-й список: {doubles_second}')

# зачет!

