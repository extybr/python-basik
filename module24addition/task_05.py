""" Задача 1. Машина 3

Вам предстоит снова немного видоизменить класс Toyota из прошлого
урока. На всякий случай вот описание класса.
Четыре атрибута:
    цвет машины (например, красный),
    цена (один миллион),
    максимальная скорость (200),
    текущая скорость (ноль).
Два метода:
    Отображение информации об объекте класса.
    Метод, который позволяет устанавливать текущую скорость машины.
Теперь все четыре атрибута должны инициализироваться при создании
экземпляра класса (то есть передаваться в init). Реализуйте такое
изменение класса. """

class Car:

    def __init__(self, color, price, max_speed, actual_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.actual_speed = actual_speed

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nActual speed: {}'.format(
            self.color, self.price, self.max_speed, self.actual_speed))


my_car = Car('red', 1000_000, 200, 20)
my_car.info()

