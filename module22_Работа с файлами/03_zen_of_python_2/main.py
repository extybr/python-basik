import os

path = os.path.join('..', '02_zen_of_python', 'zen.txt')
print('Относительный путь:', path)
size = os.path.getsize(path)
print('Размер файла:', size, 'Byte')

zen = open(path, 'r')
for count, row in enumerate(zen, 1):
    if row[-1] == '!':
        print('Количество строк в файле:', count)

zen = open(path, 'r')
count = 0
for word in zen:
    count += len(word.split())
    # row = word.split()
    # print(len(row), row)
print('Количество слов в файле:', count)

zen = open(path, 'r')
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
count = 0
zen_letters = []
for line in zen.readlines():
    for letter in line:
        if letter not in ".,!-'* \n":
            # print(letter)
            count += 1
            zen_letters.append(letter.lower())
print('Количество букв в файле:', count)

# temp = 'a'
# for letter in alphabet:
#     if 0 < zen_letters.count(letter) < zen_letters.count(temp):
#         temp = letter
# print(f'Наиболее редкая буква <{temp}>, встречается в тексте {zen_letters.count(temp)} раза.')

numbers = [zen_letters.count(letter) for letter in alphabet]
minimum_count = min(number for number in numbers if number > 0)
minimum_letter = alphabet[numbers.index(minimum_count)]
print(f'Наиболее редкая буква <{minimum_letter}>, встречается в тексте {minimum_count} раза.')

zen.close()
