
number = int(input('Кол-во клеток: '))
item = []
bad_indicator = ''
for index in range(1, number + 1):
    indicator = int(input(f'Эффективность {index}-ой клетки: '))
    item.append(indicator)
    if indicator < index:
        bad_indicator += str(indicator) + ' '
print(item)

print(f'Неподходящие значения: {bad_indicator}')

# зачет!
