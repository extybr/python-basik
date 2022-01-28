
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

my_detail = input('Название детали: ')

detail_count, detail_summa = 0, 0
for detail, cost in shop:
    if detail == my_detail:
        detail_count += 1
        detail_summa += cost

print(f'Кол-во деталей - {detail_count}')
print(f'Общая стоимость - {detail_summa}')

# зачет!
