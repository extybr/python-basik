print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Введите размер стипендии: '))
expenses = int(input('Введите расходы на проживание: '))
money_perents = 0
money_year = 0
for month in range(1, 11):
    inflation = expenses / 100 * 3
    if month == 1:
        inflation = 0
    expenses += inflation
    money_perents = expenses - educational_grant
    money_year += money_perents
print('Небходимо взять у родителей ', money_year, ' рублей.')