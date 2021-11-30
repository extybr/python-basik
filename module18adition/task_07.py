""" Задача 1. Шифр Цезаря 2

#  Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу. 

#  Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре. """

def encryption_of_text(alphabet, text, shift):
    letters = [(alphabet[(alphabet.index(symbol) + shift) % 33] if symbol != ' ' else ' ') for symbol in text]
    new = ''.join(letters)
    return new


rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЬЭЮЯ'.lower()
my_text = input('Введите сообщение: ').lower()
my_shift = int(input('Введите сдвиг: '))

encode = encryption_of_text(rus_alphabet, my_text, my_shift)
print(f'Зашифрованное сообщение: {encode}')

