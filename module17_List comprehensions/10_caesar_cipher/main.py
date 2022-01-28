
def encryption_of_text(alphabet, text, shift):
    letters = [(alphabet[(alphabet.index(symbol) + shift) % 33] if symbol != ' ' else ' ') for symbol in text]
    new = ''
    for letter in letters:
        new += letter
    return new


rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЬЭЮЯ'.lower()
my_text = input('Введите сообщение: ').lower()
my_shift = int(input('Введите сдвиг: '))

encode = encryption_of_text(rus_alphabet, my_text, my_shift)
print(f'Зашифрованное сообщение: {encode}')

# зачет!

