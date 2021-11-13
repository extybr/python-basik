
def revers_symbols(number):
    right_symbol = temp_symbol = left_symbol = ''
    for symbol in str(number):
        if symbol == '.':
            left_symbol = temp_symbol
            right_symbol = ''
            continue
        right_symbol += symbol
        temp_symbol += symbol
    right = revers_number(right_symbol)
    left = revers_number(left_symbol)
    number_symbol = left + '.' + right
    return float(number_symbol)


def revers_number(numbers):
    revers = ''
    numbers = int(numbers)
    while numbers > 0:
        last_number = numbers % 10
        numbers //= 10
        revers += str(last_number)
    return revers


first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
first_revers = revers_symbols(first)
second_revers = revers_symbols(second)
print('Первое число наоборот:', first_revers)
print('Второе число наоборот:', second_revers)
summa = first_revers + second_revers
print('Сумма:', summa)

# зачет!
