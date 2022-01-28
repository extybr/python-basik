
word = input('Введите слово: ')
index = 0
temp = False
while len(word) // 2 != index:
    end = word[len(word) - index - 1]
    if word[index] == end:
        temp = True
    elif word[index] != end:
        temp = False
        break
    index += 1
if temp:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# зачет!
