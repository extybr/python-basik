
first = []
for index in range(1, 4):
    number = int(input(f'Введите {index} число 1-го списка: '))
    first.append(number)

second = []
for index in range(1, 8):
    number = int(input(f'Введите {index} число 2-го списка: '))
    second.append(number)

print(f'Первый список: {first}')
print(f'Второй список: {second}')

first.extend(second)
# first = list(set(first))

for index in first:
    while first.count(index) > 1:
        first.remove(index)

print(f'Новый первый список с уникальными элементами: {first}')

# зачет!
