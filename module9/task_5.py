print('Задача 5. Марсоход 2')

# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
#
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
#
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
#
# Пример:
#
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

print('Доступные команды для перемещения робота: W/S/A/D')
coordinate_x = 8
coordinate_y = 10

while True:
    command = input('Марсоход находится на позиции ' + str(coordinate_x) +
                    ',' + str(coordinate_y) + ' введите команду: ')
    if command == 'A' and coordinate_x != 15:
        coordinate_x += 1
    elif command == 'D' and coordinate_x != 0:
        coordinate_x -= 1

    elif command == 'W' and coordinate_y != 20:
        coordinate_y += 1
    elif command == 'S' and coordinate_y != 0:
        coordinate_y -= 1
