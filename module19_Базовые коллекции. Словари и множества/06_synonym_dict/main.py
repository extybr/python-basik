
numbers = int(input('Введите количество пар слов: '))
dictionary = dict()
for index in range(1, numbers + 1):
    text = input(f'{index} пара: ').lower().split()
    dictionary[text[0]] = text[-1]
# print(dictionary)

synonym = input('Введите слово: ').lower()
for key, value in dictionary.items():
    if value == synonym:
        print(f'Синоним: {key}')
        break
    if key == synonym:
        print(f'Синоним: {value}')
        break
else:
    print('Такого слова в словаре нет.')
