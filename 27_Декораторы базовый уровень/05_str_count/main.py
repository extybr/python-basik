from typing import Callable, Any
import functools


def counter(function: Callable) -> Callable:
    """ Количество вызовов декорируемой функции """
    @functools.wraps(function)
    def wrapped_function(*args, **kwargs) -> Any:
        wrapped_function.count += 1
        result = function(*args, **kwargs)
        return result, wrapped_function.__dict__   # {function.__name__: wrapped_function.count}
    wrapped_function.count = 0
    return wrapped_function


@counter
def task1():
    """ Выполнение задачи """
    return 'Задача выполнена'


@counter
def task2():
    """ Выполнение задачи """
    return 'Задача выполнена'


for _ in range(10):
    print(task1())
print(task2())
