""" Задача 1. Машина

Напишите класс Toyota, состоящий из четырёх статических атрибутов: 
    цвет машины (например, красный),
    цена (один миллион),
    максимальная скорость (200),
    текущая скорость (ноль).
Создайте три экземпляра класса и каждому из них поменяйте значение
текущей скорости на случайное число от нуля до 200. """

import random


class Car:
    color = 'yellow'
    price = 1000_000
    max_speed = 200
    actual_speed = 0


first_car = Car()
second_car = Car()
firthd_car = Car()
first_car.actual_speed = random.randint(0, 200)
second_car.actual_speed = random.randint(0, 200)
firthd_car.actual_speed = random.randint(0, 200)
print(first_car.actual_speed)

