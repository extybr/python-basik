print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number = int(input('Введите число: '))
for row in range(1, number + 1):
    for col in range(1, number + 1):
        if row < col:
            print(' ', end='\t')
        elif row == col or row > col:
            print(row, end='\t')
    print()
