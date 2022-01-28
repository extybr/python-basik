
numbers = int(input('Введите кол-во заказов: '))
base = dict()
for number in range(1, numbers + 1):
    fio, pizza, amount = input(f'{number} заказ: ').split()
    if not base.get(fio):
        base[fio] = {pizza: int(amount)}
    else:
        if not base.get(fio, {}).get(pizza, {}):
            # base[fio] |= {pizza: int(amount)}
            base[fio].update({pizza: int(amount)})
        else:
            base[fio][pizza] += int(amount)

# print(base)
for key, value in base.items():
    print(f'{key}:')
    for item in value:
        print(f'      {item}: {value[item]}')
	
		
"""		
numbers = int(input('Введите кол-во заказов: '))
base = dict()
for number in range(1, numbers + 1):
    order = input(f'{number} заказ: ').split()
    if not base.get(order[0]):
        base[order[0]] = {order[1]: int(order[2])}
    else:
        if not base.get(order[0], {}).get(order[1], {}):
            # base[order[0]] |= {order[1]: int(order[2])}
            base[order[0]].update({order[1]: int(order[2])})
        else:
            base[order[0]][order[1]] += int(order[2])

# print(base)
for key, value in base.items():
    print(f'{key}:')
    for item in value:
        print(f'      {item}: {value[item]}')
"""