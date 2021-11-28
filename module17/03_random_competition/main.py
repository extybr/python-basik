
import random

first = [round(random.uniform(5, 10), 2) for _ in range(20)]
second = [round(random.uniform(5, 10), 2) for _ in range(20)]
winner = [(first[index] if first[index] > second[index] else second[index]) for index in range(20)]

print(f'Первая команда: {first}')
print(f'Вторая команда: {second}')
print(f'Победители тура: {winner}')

# зачет!
