
game = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
data = dict()
for index in range(1, game + 1):
    result, name = input(f'{index} запись: ').split()
    if not data.get(name, {}):
        data[name] = int(result)
    else:
        if int(result) > int(data.get(name)):
            data[name] = int(result)
# print(data)
print('\nИтоги соревнований:')
point = 0
for value in reversed(sorted(data.values())):
    for key in data.keys():
        if value == data[key]:
            if point == 3:
                break
            point += 1
            print(f'{point} место. {key} ({value})')

# зачет!

