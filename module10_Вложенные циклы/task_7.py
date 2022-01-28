print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

summa = 0
maximum_summa = 0
maximum_number = 0
cycle = int(input('Сколько цифр будет вводиться: '))

for numbers in range(1, cycle + 1):
    number = int(input('Введите ' + str(numbers) + ' число: '))
    temp = number

    while number > 0:
        summa += number % 10
        number //= 10
    if number == 0:
        summa += number
        #print(summa)

    if summa > maximum_summa:
        maximum_summa = summa
        maximum_number = temp
    summa = 0

print('Наибольшая сумма: ', maximum_summa, '\nНаибольшее число: ',
      maximum_number)
