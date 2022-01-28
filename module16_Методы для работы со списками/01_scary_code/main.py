
first = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]

for index in second:
    first.append(index)

temp = 0
for index in first:
    if index == 5:
        temp += 1
print(f'Кол-во цифр 5 при первом объединении: {temp}')

for index in first:
    if index == 5:
        first.remove(index)

for index in third:
    first.append(index)

temp = 0
for index in first:
    if index == 3:
        temp += 1
print(f'Кол-во цифр 3 при втором объединении: {temp}')
print(f'Итоговый список: {first}')

# зачет!
