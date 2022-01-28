
first = int(input('Введите первый год: '))
second = int(input('Введите второй год: '))
print('Года от', first, 'до', second, 'с тремя одинаковыми цифрами:')

for year in range(first, second + 1):
    first_number = year % 10
    second_number = (year % 100) // 10
    third_number = (year // 100) % 10
    fourth_number = year // 1000
    if (
            first_number == second_number == third_number) or (
            first_number == second_number == fourth_number) or (
            second_number == third_number == fourth_number) or (
            third_number == fourth_number == first_number
    ):
        print(year)

# зачет!
