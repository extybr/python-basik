print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введите число: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

def normalize_for_ten(number):
    count = 0
    temp = number
    while number > 0:
        number //= 10
        count += 1
    exhibitor = count - 1
    any_number = temp / (10 ** exhibitor)
    print('Формат плавающей точки: x = ', any_number, ' * 10 **', exhibitor)


def normalize_for_one(number):
    count = 0
    while number < 1:
        number *= 10
        count += 1
    number = round(number, 5)
    print('Формат плавающей точки: x = ', number, ' * 10 **', -count)


my_number = float(input('Введите число: '))
if my_number >= 10:
    normalize_for_ten(my_number)
elif 1 > my_number > 0:
    normalize_for_one(my_number)
else:
    print('Ошибка ввода. Введите число больше нуля.')
