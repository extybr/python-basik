print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

number = int(input('Введите число: '))
temp = 1
for row in range(number):
    space = number - row - 1
    print('    ' * space, end = '')
    for _ in range(row + 1):
        print(temp, end = '      ')
        temp += 2
    print()
