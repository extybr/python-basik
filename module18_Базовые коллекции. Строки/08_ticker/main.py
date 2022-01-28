
def cyclic_shift(ticker, new_ticker):
    count = 0
    for _ in range(len(ticker)):
        count += 1
        ticker.insert(0, ticker.pop())
        if ticker == new_ticker:
            return print(f'Первая строка получается из второй со сдвигом {count}')
    else:
        return print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


first = input('Первая строка: ')
second = input('Вторая строка: ')
ticker_first = [items for items in first]
ticker_second = [items for items in second]
cyclic_shift(ticker_first, ticker_second)

# зачет!

