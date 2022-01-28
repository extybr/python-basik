
word = input('Введите слово: ')
count = 0
item = []
for symbol in word:
    if symbol in item and word:
        continue
    item.append(symbol)
    count += 1
print('Кол-во уникальных букв:', count)
# print(item)

# зачет!
