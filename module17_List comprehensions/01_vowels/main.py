
text = input('Введите текст: ')

alphabet = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']

new = [index for index in text if index in alphabet]

length = len(new)
print(f'Список гласных букв: {new}')
print(f'Длина списка: {length}')

# зачет!
