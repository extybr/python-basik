
import math


def checking_coordinates(horizontal, vertical, circle):
    hypotenuse = math.hypot(horizontal, vertical)
    if hypotenuse <= circle:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
coordinate_x = float(input('X: '))
coordinate_y = float(input('Y: '))
radius = float(input('Введите радиус: '))
checking_coordinates(coordinate_x, coordinate_y, radius)

# зачет!

