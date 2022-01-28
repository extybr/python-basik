
def output(stop_number, start_number):
    if start_number == stop_number + 1:
        return start_number
    print(start_number)
    output(stop_number, start_number + 1)


number = int(input('Введите число: '))
output(number, 1)
