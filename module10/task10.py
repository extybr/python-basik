print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

depth = int(input('Введите глубину ямы: '))
for row in range(depth):
    content = depth - row
    for left in range(depth, (content - 1), -1):
        print(left, end = '')

    point = 2 * (content - 1)
    print('.' * point, end = '')

    for right in range(content, depth + 1):
        print(right, end = '')
    print()
