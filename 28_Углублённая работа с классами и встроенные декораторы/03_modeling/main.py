class Square:
    """
    Квадрат. Родительский класс
    """
    def __init__(self, length: float) -> None:
        """
        Конструктор класса
        :param length: float
        """
        self.length = length

    @property
    def area_square(self) -> float:
        """
        Вычисление площади
        :return: float
        """
        return self.length ** 2

    @property
    def perimeter_square(self) -> float:
        """
        Вычисление периметра
        :return: float
        """
        return self.length * 4

    @area_square.setter
    def area_square(self, length: float) -> None:
        """
        Setter
        :param length: float
        :return: None
        """
        if length < 0:
            raise Exception('Сторона не может быть меньше нуля')

    @perimeter_square.setter
    def perimeter_square(self, length: float) -> None:
        """
        Setter
        :param length: float
        :return: None
        """
        if length < 0:
            raise Exception('Сторона не может быть меньше нуля')


class Triangle:
    """
    Треугольник. Родительский класс
    """
    def __init__(self, length: float, height: float) -> None:
        """
        Конструктор класса
        :param length: float
        :param height: float
        """
        self.length = length
        self.height = height

    @property
    def area_triangle(self) -> float:
        """
        Вычисление площади
        :return: float
        """
        return self.length * self.height / 2

    @area_triangle.setter
    def area_triangle(self, height) -> None:
        if height < 0:
            raise Exception('Высота не может быть меньше нуля')

    @property
    def perimeter_triangle(self) -> float:
        """
        Вычисление периметра
        :return: float
        """
        return 2 * ((self.length ** 2 + self.height ** 2) ** 0.5) + 2 * self.length

    @perimeter_triangle.setter
    def perimeter_triangle(self, height) -> None:
        """
        Setter
        :return: None
        """
        if height < 0:
            raise Exception('Высота не может быть меньше нуля')


class ResultMixin:
    """
    Класс вычисления сложных фигур
    """
    @classmethod
    def area(cls, figure: list) -> float:
        """
        Вычисление площади фигуры
        :param figure: float
        :return: float
        """
        summa = 0
        for item in figure:
            if item.__class__ == Square:
                summa += item.area_square
            elif item.__class__ == Triangle:
                summa += item.area_triangle
        return summa

    @classmethod
    def perimeter(cls, figure: list) -> float:
        """
        Вычисление периметра фигуры
        :param figure: float
        :return: float
        """
        summa = 0
        for item in figure:
            if item.__class__ == Square:
                summa += item.perimeter_square
            elif item.__class__ == Triangle:
                summa += item.perimeter_triangle
        return summa


class Cube(Square, ResultMixin):
    """
    Куб. Дочерний класс от "Квадрата"
    """
    def __init__(self, length: float) -> None:
        """
        Конструктор класса
        :param length: float
        """
        super().__init__(length)
        self.figure = [Square(length) for _ in range(6)]


class Pyramid(Triangle, ResultMixin):
    """
    Пирамида. Дочерний класс от "Треугольника"
    """
    def __init__(self, length: float, height: float) -> None:
        """
        Конструктор класса
        :param length: float
        :param height: float
        """
        super().__init__(length, height)
        self.figure = [Triangle(length, height), Triangle(length, height), Triangle(
            length, height), Triangle(length, height), Square(length)]


side = 4
side_height = 5
square = Square(side)
# square.area_square = -4  # проверка на отрицательное значение
square_area = round(square.area_square, 2)
square_perimeter = round(square.perimeter_square, 2)
print(f'Площадь квадрата: {square_area}, Периметр квадрата: {square_perimeter}')
triangle = Triangle(side, side_height)
# triangle.perimeter_triangle = -5  # проверка на отрицательное значение
triangle_area = round(triangle.area_triangle, 2)
triangle_perimeter = round(triangle.perimeter_triangle, 2)
print(f'Площадь треугольника: {triangle_area}, '
      f'Периметр треугольника: {triangle_perimeter}')
cube = Cube(side)
cube_area = round(cube.area(cube.figure), 2)
cube_perimeter = round(cube.perimeter(cube.figure), 2)
print(f'Площадь куба: {cube_area}, Периметр куба: {cube_perimeter}')
pyramid = Pyramid(side, side_height)
pyramid_area = round(pyramid.area(pyramid.figure), 2)
pyramid_perimeter = round(pyramid.perimeter(pyramid.figure), 2)
print(f'Площадь пирамиды: {pyramid_area}, '
      f'Периметр пирамиды: {pyramid_perimeter}')
