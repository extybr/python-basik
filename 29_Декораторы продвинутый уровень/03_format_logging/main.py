from typing import Callable
import functools
import time


def logging(time_format: str, cls_name: str, function: Callable) -> Callable:
    """
    Логирование метода класса, замер времени работы метода
    :param time_format: str
    :param cls_name: str
    :param function: Callable
    :return: Callable
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        # month = ["", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа",
        #          "сентября", "октября", "ноября", "декабря"]
        # localtime = time.localtime()
        # full_time = (f'{localtime[2]} {month[localtime[1]]} {localtime[0]} - {localtime[3]}'
        #              f':{localtime[4]}:{localtime[5]}')

        new_time = ''.join([f'%{letter}' if letter.isalpha() else letter for letter in time_format])
        full_time = time.strftime(new_time)
        print('- Запускается: {}.{}. Дата и время запуска: {}'
              .format(cls_name, function.__name__, full_time))
        start = time.time()
        result = function(*args, **kwargs)
        finish = round((time.time() - start), 3)
        print("- Завершение {}.{}. Время работы метода - {}s"
              .format(cls_name, function.__name__, finish))
        return result
    return wrapper


def log_methods(time_format: any) -> Callable:
    """
    Функция декоратор для всех методов класса, кроме магических
    :param time_format: any
    :return:  Callable
    """
    @functools.wraps(time_format)
    def decorator_method(cls):
        for method in dir(cls):
            if method.startswith('__') is False:
                new_method = getattr(cls, method)
                decorated_method = logging(time_format, cls.__name__, new_method)
                setattr(cls, method, decorated_method)
        return cls
    return decorator_method


@log_methods("b d Y - H:M:S")
class Human:
    def test_summa_1(self) -> int:
        """
        Функция возвращает результат мат.операции
        :return: int
        """
        print('Тут метод test summa 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([item ** 2 for item in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class Man(Human):
    def test_summa_1(self) -> None:
        super().test_summa_1()
        print("Тут метод test summa 1 у наследника")

    def test_summa_2(self) -> int:
        """
        Функция возвращает результат мат.операции
        :return: int
        """
        print("Тут метод test summa 2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([item ** 2 for item in range(10000)])
        return result


my_object = Man()
my_object.test_summa_1()
my_object.test_summa_2()
