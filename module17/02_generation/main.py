
import random

numbers = int(input('Введите длину списка: '))

generation = [random.randint(1, 10) for _ in range(numbers)]

new_generation = [(1 if index % 2 == 0 else index % 5) for index in range(len(generation))]
print(f'Результат: {new_generation}')

# зачет!
