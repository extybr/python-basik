
def least_common_multiplier(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    print('Наименьший делитель, отличный от единицы:', divider)


my_number = int(input('Введите число: '))
least_common_multiplier(my_number)

# зачет!
