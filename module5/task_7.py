print('Задача 7. Костя хочет выигрывать')

# После игры в кубики Костя захотел немного изучить работу игровых автоматов,
# а заодно математику и теорию вероятностей.
# Но ему нужно с чего-то начать:
# написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.

# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
if number_1 == number_2 == number_3:
    print('Совпадений: 3')
elif (number_1 == number_2) or (number_1 == number_3) or (number_2 == number_3):
    print('Совпадений: 2')
else:
    print('Совпадений: 0')
