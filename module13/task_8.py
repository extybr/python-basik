print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

precision = float(input('Введите точность: '))
number = float(input('Введите x: '))

temp = count = summa_row = 0
unit = result = multiplication = factorial = 1
while precision < abs(result - temp):
    temp = result
    summa_row = unit * multiplication / factorial
    unit *= -1
    count += 1
    multiplication *= number * number
    factorial *= 2 * count * (2 * count - 1)
    result += summa_row
print('Сумма ряда =', (result - 1))
