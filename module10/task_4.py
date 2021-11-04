print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^

side = int(input('Введите размеры сторон квадрата: '))
for row in range(side):
    for col in range(side):
        if row == col:
            print('^', end = '')
        elif col == -row + (side - 1):
            print('^', end = '')
        else:
            print(' ', end = '')
    print()