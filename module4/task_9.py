print('Задача 9. Плохой циферблат')

# У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега,
# но он постоянно глючит и сбрасывается.
# Саша заметил закономерность:
# каждый раз, когда сумма цифр на циферблате превышает число текущего дня,
# циферблат сбрасывается.

# Напишите программу,
# которая получает на вход от пользователя два числа: пробег и номер дня (первое — обязательно трёхзначное),
# затем находит сумму цифр первого числа,
# и если эта сумма больше второго числа,
# выводит сообщение: «Сброс», — и сбрасывает пробег до нуля.
# В противном случае выводится: «Сегодня не сломался».
# В конце также выводится сам пробег.

mileage = int(input('Введите пробег: '))
day = int(input('Введите сегодняшнее число: '))
summa = mileage // 100 + mileage % 100 // 10 + mileage % 10
if day < summa:
    print('Сброс.')
    print('Пробег: 0')
else:
    print('Сегодня не сломался.')
    print('Пробег: ', mileage)
