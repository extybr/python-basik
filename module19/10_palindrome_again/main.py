
text = input('Введите строку: ')
count = 0
for letter in set(text):
    count += (text.count(letter) % 2)
if count > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
# print(count)
