print('Задача 9. Выражение')

#Дано число x.
#Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))


result = 1
number_x = int(input('Введите число: '))
for number in range(1, 7):
    result *= (number_x - (2 ** number - 1)) / (number_x - 2 ** number)
print('Результат: ', result)
