
text = input('Введите строку: ')
compression = ''
text += '1'
temp = text[0]
count = 0
for items in text:
    if temp != items:
        compression += temp + str(count)
        temp = items
        count = 0
    count += 1
print(f'\nЗакодированная строка: {compression}')

# зачет!
