
def main():
    return print(f'Ответ в консоли: {new_crypto}')


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return number == divider


def crypto(my_data):
    elements = list()
    for index in range(2, len(my_data)):
        if is_prime(index):
            elements.append(my_data[index])
    return elements


data = input('Введите данные: ')
# new_crypto = crypto('О Дивный Новый мир!')
# new_crypto = crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_crypto = crypto(data)
main()

# зачет!

