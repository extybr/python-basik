from typing import Callable, Any
from datetime import datetime
import functools


def logging(function: Callable) -> Callable:
    """ Логирование функции """
    @functools.wraps(function)
    def wrapped_function(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as error:
            bug_time = str(datetime.today())[:19]
            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(f'Название функции: {function.__name__}\nВремя: {bug_time}\n'
                          f'Описание ошибки: {error}\n*****************************\n')
    return wrapped_function


@logging
def my_function() -> Any:
    """ Документация функции """
    # print('Hello World')
    return f'{my_function.__name__}, {my_function.__doc__}'


print(my_function())
print(my_function(100, 'fail', 3.14))  # имитируем ошибку
# print(logging.__doc__)
