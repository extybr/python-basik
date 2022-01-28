print('Задача 9. Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0. 
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
# 
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число, 
# если нет корней — не выводите ничего

import math

coefficient_a = float(input('Введите коэффициент a: '))
coefficient_b = float(input('Введите коэффициент b: '))
coefficient_c = float(input('Введите коэффициент c: '))
discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
if discriminant < 0:
    print('Корней нет')
elif discriminant > 0:
    root_x1 = (-coefficient_b + math.sqrt(discriminant)) / 2 * coefficient_a
    root_x2 = (-coefficient_b - math.sqrt(discriminant)) / 2 * coefficient_a
    if root_x1 > root_x2:
        print('Корни квадратного уравнения: ', root_x1, root_x2)
    else:
        print('Корни квадратного уравнения: ', root_x2, root_x1)
else:
    root_x1 = (-coefficient_b + math.sqrt(discriminant)) / 2 * coefficient_a
    print('Корень квадратного уравнения: ', root_x1)
