print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.


def main_program():
    choice = int(input('Введите действие, которое нужно с ним сделать: \n1 - вывести сумму его цифр\n2 - вывести максимальную цифру\n3 - вывести минимальную цифру\n: '))
    if choice == 1:
        calculate_summa(my_number)
    elif choice == 2:
        calculate_maximum(my_number)
    elif choice == 3:
        calculate_minimum(my_number)
    else:
        print('Ошибка ввода.\n')
    main_program()


def calculate_summa(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    print('Сумма чисел:', summ, '\n')


def calculate_maximum(number):
    max_number = 0
    while number > 0:
        temp = number % 10
        if temp > max_number:
            max_number = temp
        number //= 10
    print('Максимальное число:', max_number, '\n')


def calculate_minimum(number):
    min_number = number
    while number > 0:
        temp = number % 10
        if min_number > temp:
            min_number = temp
        number //= 10
    print('Минимальное число:', min_number, '\n')


my_number = int(input('Введите число: '))

main_program()
