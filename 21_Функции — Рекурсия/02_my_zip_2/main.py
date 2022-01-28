
def analog_zip(one, two):
    first, second = tuple(one), tuple(two)
    full = [(first[index], second[index]) for index in range(min(len(first), len(second)))]
    # for index in range(min(len(first), len(second))):
    # print((first[index], second[index]))  # вывод попарно
    print(full)  # вывод список пар


string = 'ABCDN'
numbers_t = (10, 20, 30, 40)
numbers_l = [11, 22, 33, 44]
dictionary = {'15': 3, 'X': 9, 'i': 9, 'g': 0}
analog_zip(string, numbers_l)
analog_zip(numbers_t, string)
analog_zip(numbers_t, dictionary)
