from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """
    Декоратор дает другому декоратору принимать произвольные аргументы
    :param decorator_to_enhance: Callable
    :return: Callable
    """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(function: Callable) -> Callable:
            return decorator_to_enhance(function, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(function: Callable, *dec_args, **dec_kwargs) -> Callable:
    """
    Декоратор - шаблон
    :param function: Callable
    :param dec_args:
    :param dec_kwargs:
    :return: Callable
    """
    @functools.wraps(function)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор:', dec_args, dec_kwargs)
        return function(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, number: int) -> None:
    """
    Пример, декорируемой функции
    :param text: str
    :param number: int
    :return: None
    """
    print("Привет", text, number)


decorated_function("Юзер", 101)
