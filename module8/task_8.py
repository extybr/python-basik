print('Задача 8. Сумма ряда')

# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 

result = 0
number_n = int(input('Введите число: '))
for number in range(0, number_n + 1):
    divider = (-1) ** number * 1 / (2 ** number)
    result += divider
print('Результат вычисления: ', result)