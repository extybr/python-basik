""" Задача 3. Повышение цен

#  Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.

#  Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год. """

years = int(input('Сколько лет наблюдаем: '))
numbers = int(input('Сколько товаров для наблюдения: '))
my_price = []
for i in range(numbers):
    price = float(input('Цена на товар: '))
    my_price.append(price)
summa = round(sum(my_price), 2)
my = [summa]
for i in range(1, years + 1):
    inflation = int(input(f'Повышение на {i}-й год: '))
    my_inflation = [j + j * inflation / 100 for j in my_price]
    summa_inflation = round(sum(my_inflation), 2)
    my.append(summa_inflation)
print('Сумма цен за каждый год: ')
[print(i, end=' ') for i in my]
