class Circle:
    def __init__(self, horizontal, vertical, radius):
        self.radius = radius
        self.horizontal = horizontal
        self.vertical = vertical

    def output(self):
        print('\nx =', self.horizontal, ', y =', self.vertical, ',  radius =', self.radius)

    def calculate(self):
        area = 3.1415 * self.radius * self.radius
        print('Площадь окружности:', area)
        length = 2 * 3.1415 * self.radius
        print('Длина окружности:', length)

    def transform(self):
        return [self.horizontal, self.vertical, self.radius]

    def crossing(self, coordinates_1, coordinates_2):
        distance = coordinates_1[2] + coordinates_2[2]
        delta_x = coordinates_1[0] - coordinates_2[0]
        delta_y = coordinates_1[1] - coordinates_2[1]
        if delta_x ** 2 + delta_y ** 2 <= distance ** 2:
            print('\nОкружности пересекаются')

    def increase(self, times):
        self.radius *= times
        print(f'\n{times}-x кратное увеличение: x = {self.horizontal}, y = {self.vertical}, '
              f'radius = {self.radius}')


circle_1 = Circle(0, 0, 1)
circle_2 = Circle(1, 2, 2)
circle_1.output()
circle_1.calculate()
circle_2.output()
circle_2.calculate()
coordinates_circle_1 = circle_1.transform()
coordinates_circle_2 = circle_2.transform()
circle_1.crossing(coordinates_circle_1, coordinates_circle_2)
circle_1.increase(3)
