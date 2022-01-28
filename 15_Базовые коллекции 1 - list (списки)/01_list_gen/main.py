
number = int(input('Введите целое число: '))

odd_numbers = []
for index in range(1, number + 1):
    if index % 2 != 0:
        odd_numbers.append(index)
print(odd_numbers)

# зачет!
