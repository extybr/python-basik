
def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


my_number = int(input('Введите позицию числа в ряде Фибоначчи: '))
number_position = fibonacci(my_number)
print(number_position)

# зачет!
