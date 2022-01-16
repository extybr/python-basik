""" Задача 2. Координаты точки

Объект «Точка» на плоскости имеет координаты X и Y. При
создании новой точки могут передаваться пользовательские
значения координат, по умолчанию x = 0, y = 0. 

Реализуйте класс, который будет представлять эту точку,
и напишите метод, который предоставляет информацию о ней.
Также внутри класса пропишите счётчик, который будет отвечать
за количество созданных точек.

Подсказка: счётчик можно объявить внутри самого класса и
увеличивать его в методе __init__. """

import random


class Point:

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
        self.count = 0

    def info(self, count):
        self.count = count + 1
        print('X: {}\nY: {}\nCount: {}'.format(self.horizontal, self.vertical, self.count))


my_car = Point(0, 0)
my_car.info(0)
for i in range(1, 5):
    first = random.randint(1, 10)
    second = random.randint(1, 10)
    my_car = Point(first, second)
    my_car.info(i)

