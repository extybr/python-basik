
with open('text.txt', 'w') as text:
    text.write('Hello\n' * 4)

with open('text.txt', 'r') as text:
    print('Содержимое файла text.txt:\n', text.read())

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = open('text.txt', 'r')
cipher = open('cipher_text.txt', 'w')
for row, line in enumerate(text.readlines(), 1):
    cipher.write('\n')
    for letter in line:
        if letter == line[-1]:
            continue
        cipher_letter = alphabet[alphabet.find(letter) + row]
        cipher.write(cipher_letter)
cipher.close()
text.close()

with open('cipher_text.txt', 'r') as cipher:
    print('Содержимое файла cipher_text.txt:', cipher.read())
