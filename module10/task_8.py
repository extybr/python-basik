print('Задача 8. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

height = int(input('Введите высоту пирамиды: '))
for numbers in range(height):
    symbol_1 = height - numbers - 1
    symbol_2 = numbers * 2 + 1
    print(' ' * symbol_1 + '#' * symbol_2)
