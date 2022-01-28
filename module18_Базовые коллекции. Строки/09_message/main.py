
def reverse_text(text, symbol):
    new_text = []
    for index in text:
        index = index[::-1]
        if index[0] in symbol:
            index = index[1:] + index[0]
        new_text.append(index)
    return new_text


my_text = input('Сообщение: ').split()
# my_text = 'Это задание, очень! простое.'.split()
special_symbol = '.,!:;?'
reverse = reverse_text(my_text, special_symbol)
message = ''
for items in reverse:
    message += items + ' '
print(f'\nНовое сообщение: {message}')

# зачет!
