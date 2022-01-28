print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def computation_summa(my_number):
    summa = 0
    count = 0
    for numbers in range(1, my_number + 1):
        summa += numbers
        count += 1
    print('Я знаю, что сумма чисел от 1 до ' + str(my_number) + ' равна', summa)


number = int(input('Введите целое положительное число: '))

computation_summa(number)
