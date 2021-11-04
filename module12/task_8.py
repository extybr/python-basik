print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def computation_divider(first, second):
    while second != 0:
        first, second = second, (first % second)
    print('Наибольший общий делитель:', first)


first_1 = float(input('Введите первое число: '))
second_2 = float(input('Введите второе число: '))

computation_divider(first_1, second_2)
