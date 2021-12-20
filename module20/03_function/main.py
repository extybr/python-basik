
def transform(data, element):
    selection = list()
    count = 0
    # for index in range(len(crypto_text)): // для глубины
    for item in data:
        if item == element:
            count += 1
        if count == 1:
            selection.append(item)
        elif count == 2:
            selection.append(item)
            return tuple(selection)
    return tuple(selection)


my_element = input('Введите элемент для поиска: ')
slicer = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
# slicer = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'e', 'e', 'l')
# slicer = tuple([input('Введите элемент: ') for symbol in range(5)])
if str(my_element).isdigit():
    new_slicer = transform(slicer, int(my_element))
else:
    new_slicer = transform(slicer, my_element)

print(f'Ответ в консоли: {new_slicer}')

# зачет!

