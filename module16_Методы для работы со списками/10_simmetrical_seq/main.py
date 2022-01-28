
def palindrome(number_forward):
    reverse_number = []
    for items in range(len(number_forward) - 1, -1, -1):
        reverse_number.append(number_forward[items])
    if number_forward == reverse_number:
        return True
    else:
        return False


def sequence_of_numbers(sequence_amount):
    sequence = ''
    for items in sequence_amount:
        sequence += str(items) + ' '
    return sequence


numbers = int(input('Кол-во чисел: '))
amount_numbers = []

for index in range(numbers):
    number = int(input('Число: '))
    amount_numbers.append(number)

temp_amount_numbers = []
new_amount_numbers = []
for index in range(numbers):
    for element in range(index, numbers):
        temp_amount_numbers.append(amount_numbers[element])
    if palindrome(temp_amount_numbers):
        for run in range(index):
            new_amount_numbers.append(amount_numbers[run])
        new_amount_numbers.reverse()
        break
    temp_amount_numbers = []

my_sequence = sequence_of_numbers(amount_numbers)
print(f'\nПоследовательность: {my_sequence}')
amount = len(new_amount_numbers)
print(f'Нужно приписать чисел: {amount}')
missing_numbers = sequence_of_numbers(new_amount_numbers)
print(f'Сами числа: {missing_numbers}')

# зачет!
