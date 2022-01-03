
with open('text.txt', 'w') as text:
    text.write('mama myla ramu.')

with open('text.txt', 'r') as text:
    print(f'\nСодержимое файла text.txt: {text.read()}\n')

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
numbers, letters = dict(), list()
with open('text.txt', 'r') as text:
    for line in text.readlines():
        for letter in line:
            letters.append(letter)
        for letter in alphabet:
            if letters.count(letter) > 0:
                numbers.update({letter: letters.count(letter)})


summa = sum(numbers.values())
numbers = dict(zip(sorted(numbers, key=numbers.get, reverse=True), sorted(numbers.values())))

with open('analysis.txt', 'w') as analysis:
    for key, value in numbers.items():
        numbers[key] = round((value / summa), 3)
        # analysis.write(str('\n{:} {:.1%}'.format(key, numbers[key])))
        analysis.write(str(f'\n{key}  {numbers[key]}'))
with open('analysis.txt', 'r') as analysis:
    print('Содержимое файла analysis.txt:', analysis.read())

