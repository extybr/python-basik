
word = input('Введите предложение: ').split()
temp, maximum = 0, 0
for index in word:
    if len(index) > maximum:
        maximum = len(index)
        temp = index
print(f'Самое длинное слово: {temp}, а его длина: {maximum}')

# зачет!

