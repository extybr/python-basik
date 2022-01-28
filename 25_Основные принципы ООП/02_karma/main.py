import random


class KillError(Exception):
    def __init__(self):
        super().__init__('Убийство')


class DrunkError(Exception):
    def __init__(self):
        super().__init__('Пьянство')


class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Автомобильная авария')


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Чревоугодие')


class DepressionError(Exception):
    def __init__(self):
        super().__init__('Депрессия')


def one_day():
    karma = random.randint(1, 7)
    number = random.randint(1, 10)
    if number == 10:
        with open('karma.log', 'a', encoding='utf-8') as karma_error:
            error = random.choice(errors)
            karma_error.write(str(error) + '\n')
            raise error
    return karma


# для правильного вывода в лог
KillError = KillError()
DrunkError = DrunkError()
CarCrashError = CarCrashError()
GluttonyError = GluttonyError()
DepressionError = DepressionError()

count, summa = 0, 0
while summa < 500:
    count += 1
    try:
        errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        summa += one_day()
    except Exception as errors:
        print(errors)
print(f'Достигнуто просвещение, после {count} дней набрано {summa} очков кармы')
