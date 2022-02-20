from typing import Callable, Any
from bs4 import BeautifulSoup
import requests
from time import time, sleep
from timeit import timeit

URL1 = 'https://cbr.ru/key-indicators/'
URL2 = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
link1 = 'https://cbr.ru'
link2 = 'https://coinmarketcap.com'

headers1 = {
    'Host': f'{link1}',
    'User-Agent': 'Mozilla/5.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

headers2 = headers1
headers2['Host'] = link2


def timer(function: Callable) -> Callable:
    """
    Создаем задержки и вычисляем полное время парсинга
    """
    start = time()
    sleep(2)

    def wrapped_function(*args, **kwargs) -> Any:
        sleep(1)
        result = function(*args, **kwargs)
        sleep(1)
        finish = time()
        timestamp = round((finish - start), 2)
        print('Задержка', timestamp, 'sec')
        return result
    return wrapped_function


@timer
def extract_dollar(url, headers) -> None:
    result = requests.get(url, headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('td', class_='value td-w-4 _bold _end mono-num _with-icon _up _red')
    result = str(results)[66:73]
    print('Курс доллара:', result, 'рублей')


@timer
def extract_bitcoin(url, headers) -> None:
    result = requests.get(url, headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', class_='priceValue')
    result = str(results)[31:38]
    print('Курс биткоина:', result, 'долларов')


def time_out(function: Callable) -> Callable:
    """ Отдельная функция-пауза """
    def wrapped_function(*args, **kwargs) -> Any:
        sleep(1)
        return function(*args, **kwargs)
    return wrapped_function


@time_out
@timer
def sequence_numbers() -> float:
    """
    Дополнительный замер времени выполнения куска кода
    с помощью модуля «timeit»
    """
    return timeit('"-".join([str(n) for n in range(100)])')


extract_dollar(URL1, headers1)
extract_bitcoin(URL2, headers2)
print(sequence_numbers())
