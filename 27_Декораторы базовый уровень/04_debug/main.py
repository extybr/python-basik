from typing import Callable, Any
import functools


def debug(function: Callable) -> Callable:
    """ Документация """
    @functools.wraps(function)
    def wrapped_function(*args, **kwargs) -> Any:
        result = function(*args, **kwargs)
        string = f'{function.__name__}{args}, {kwargs}'.replace(',), {}', ')').replace(
            '(), {', '(').replace('), {', ' ').replace('}', ')')
        print('Вызывается:', string, '\nВернула значение:', result)
        return result
    return wrapped_function


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

