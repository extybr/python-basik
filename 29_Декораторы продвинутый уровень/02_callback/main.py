from typing import Callable, Optional
import functools
import requests

URL = 'https://www.cbr-xml-daily.ru/latest.js'
# URL = 'https://www.cbr-xml-daily.com/latest.js'  # проверка неверного адреса
LINK = 'https://www.cbr-xml-daily.ru'

HEADERS = {'Host': f'{LINK}', 'User-Agent': 'Mozilla/5.0', 'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}


def callback(_function: Optional[Callable] = None, *, url) -> Callable:
    """
    Декоратор обратного вызова
    :param _function: Optional[Callable]
    :param url: str
    :return: Callable
    """
    def decorate_function(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """
            Функция-обертка проверяет доступность сервера, в случае неверного адреса или
            недоступности сервера возвращает False
            :param args:
            :param kwargs:
            :return:
            """
            try:
                request = requests.get(url, HEADERS).reason
                print(f'Функция возвращает ответ сервера: {request}')
                return function(*args, **kwargs)
            except OSError:
                return False
        return wrapper
    if _function is None:
        return decorate_function
    return decorate_function(_function)


@callback(url=URL)
def extract_dollar(url: str, headers: dict, *value: str) -> str:
    """
    Функция парсит валютные котировки
    :param url: str
    :param headers: dict
    :param value: str
    :return: str
    """
    result = requests.get(url, headers).json()
    result_1 = round(1 / result["rates"][value[0]], 3)
    result_2 = round(1 / result["rates"][value[1]], 3)
    return f'Курс выбранной валюты: {value[0]} - {result_1} рублей, {value[1]} - {result_2} рублей'


data = extract_dollar(URL, HEADERS, 'EUR', 'USD')
if data:
    print(data)
else:
    print('Такого пути нет, либо сервер недоступен')
