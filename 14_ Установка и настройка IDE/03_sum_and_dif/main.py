
def calculate_summa(my_number):
    summ = 0
    while my_number > 0:
        summ += my_number % 10
        my_number //= 10
    print('Сумма цифр:', summ)
    return summ


def calculate_numbers(my_number):
    count = 0
    while my_number > 0:
        my_number //= 10
        count += 1
    print('Кол-во цифр в числе:', count)
    return count


number = int(input('Введите целое число: '))
summa = calculate_summa(number)
numbers = calculate_numbers(number)
difference = summa - numbers
print('Разность суммы и кол-ва цифр: ', difference)

# зачет!
