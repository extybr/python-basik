from collections.abc import Callable
import functools
from random import choice

user_permissions = ['admin', 'user_1']
current_user = choice(user_permissions)


def check_permission(user: str, selected_user: str) -> Callable:
    """
    Функция-декоратор для проверки прав пользователя, для выполнения определенных действий
    :param user: str
    :param selected_user: str
    :return: Callable
    """
    def decorate_function(function: Callable) -> Callable:
        """
        Функция, принимающая в качестве аргумента другую функцию
        :param function: Callable
        :return: Callable
        """
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """
            Функция-обертка, принимающая именованные и позиционные аргументы функции
            :param args:
            :param kwargs:
            :return:
            """
            try:
                if user == selected_user:
                    return function(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('{error}: У пользователя недостаточно прав, чтобы выполнить функцию {name}'
                      .format(error=PermissionError.__name__, name=function.__name__))
        return wrapper
    return decorate_function


@check_permission('admin', current_user)
def delete_site() -> None:
    """
    Функция, выполняемая пользователем с правами администратора
    :return: None
    """
    print('Удаляем сайт')


@check_permission('user_1', current_user)
def add_comment() -> None:
    """
    Функция, выполняемая пользователем с правами пользователя
    :return: None
    """
    print('Добавляем комментарий')


delete_site()
add_comment()
