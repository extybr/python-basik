print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

year_pay = 0
for month in range(1, 13):
    pay = int(input('Введите зарплату за ' + str(month) + ' месяц: '))
    year_pay += pay
mid_pay = year_pay // 12
print('Среднегодовая зарплата равна: ', mid_pay)
