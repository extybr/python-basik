print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей.
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.

# Напишите программу,
# которая считает количество только чётных чисел в последовательности
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.

month = 0
while True:
    days = int(input('Введите число дней: '))
    if days == 0:
        break
    elif days % 2 == 0:
        month += 1
print('Месяцев с четными днями: ', month)
