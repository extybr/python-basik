import math


class MyMath:
    @classmethod
    def calculate_length_circle(cls, radius: float) -> float:
        """
        Нахождение длины окружности
        :param radius: float
        :return: float
        """
        length_circle = 2 * math.pi * radius
        return length_circle

    @classmethod
    def calculate_area_circle(cls, radius: float) -> float:
        """
        Нахождение площади окружности
        :param radius: float
        :return: float
        """
        area_circle = math.pi * (radius ** 2)
        return area_circle

    @classmethod
    def calculate_volume_cube(cls, length: float) -> float:
        """
        Нахождение объёма куба
        :param length: float
        :return: float
        """
        volume_cube = length ** 3
        return volume_cube

    @classmethod
    def calculate_volume_parallelepiped(cls, length: float, width: float, height: float) -> float:
        """
        Нахождение объёма параллелепипеда
        :param length: float
        :param width: float
        :param height: float
        :return: float
        """
        volume_parallelepiped = length * width * height
        return volume_parallelepiped

    @classmethod
    def calculate_area_sphere(cls, radius: float) -> float:
        """
        Нахождение площади поверхности сферы
        :param radius: float
        :return: float
        """
        area_sphere = 4 * math.pi * (radius ** 2)
        return area_sphere


result_1 = round(MyMath.calculate_length_circle(radius=5), 2)
print(result_1)
result_2 = round(MyMath.calculate_area_circle(radius=6), 2)
print(result_2)
result_3 = round(MyMath.calculate_volume_cube(length=31.5), 2)
print(result_3)
result_4 = round(MyMath.calculate_volume_parallelepiped(length=3, width=5.1, height=3), 2)
print(result_4)
result_5 = round(MyMath.calculate_area_sphere(radius=6.25), 2)
print(result_5)
