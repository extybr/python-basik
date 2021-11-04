print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

def turn_over_number(number):
    numbers = ''
    while number % 10 == 0:
        number //= 10
    while number > 0:
        revers = number % 10
        number //= 10
        numbers += str(revers)
    return int(numbers)


my_number_one = int(input('Введите первое число: '))
my_number_two = int(input('Введите второе число: '))
one = turn_over_number(my_number_one)
two = turn_over_number(my_number_two)
summa = one + two
summa_revers = turn_over_number(summa)
print('Первое число наоборот:', one)
print('Второе число наоборот:', two)
print('Сумма:', summa)
print('Сумма наоборот:', summa_revers)
