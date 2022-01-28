""" Задача 1. Машина 2

Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
    цвет машины (например, красный),
    цена (один миллион),
    максимальная скорость (200),
    текущая скорость (ноль).
Добавьте два метода класса:
    Отображение информации об объекте класса.
    Метод, который позволяет устанавливать текущую скорость машины.
Проверьте работу этих методов. """

class Car:
    color = 'yellow'
    price = 1000_000
    max_speed = 200
    actual_speed = 0

    def info(self):
        print('Color: {}'.format(self.color))

    def set_sped(self, speed):
        self.actual_speed = speed


first_car = Car()
second_car = Car()
firthd_car = Car()
first_car.actual_speed = 200
second_car.actual_speed = 100
firthd_car.actual_speed = 50
print('Actual speed: {}'.format(first_car.actual_speed))
second_car.info()

