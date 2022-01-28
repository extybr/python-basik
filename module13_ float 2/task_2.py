print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

def calculate_maximum():
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    maximum = int(((first + second) + abs(first - second)) / 2)
    return maximum


def calculate_maximum_three(maximum):
    third = int(input('Введите третье число: '))
    maximum_three = int(((maximum + third) + abs(maximum - third)) / 2)
    print('Максимальное число:', maximum_three)


temp_maximum = calculate_maximum()
calculate_maximum_three(temp_maximum)
