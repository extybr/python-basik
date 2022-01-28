
friends = int(input('Кол-во друзей: '))
debt = int(input('Долговых расписок: '))
cash_balance = []
for _ in range(friends):
    cash_balance.append(0)

for index in range(debt):
    print(f'\n{index + 1} расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    cash_balance[to_whom - 1] -= how_much
    cash_balance[from_whom - 1] += how_much

print('\nБаланс друзей:')
for index in range(friends):
    cash = cash_balance[index]
    print(f'{index + 1} : {cash}')

# зачет!
