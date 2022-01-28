
def histogram(letters):
    my_letters = dict()
    for symbol in letters:
        if symbol in my_letters:
            my_letters[symbol] += 1
        else:
            my_letters[symbol] = 1
    return my_letters


def frequency_histogram(new_values, new_count):
    alphabet = list()
    for key, value in new_count.items():
        if value == new_values:
            alphabet.append(key)
    return alphabet


text = 'Здесь что-то написано'
count = histogram(text)
for items in sorted(count.keys()):
    print(items, ':',  count[items])

print('\nИнвертированный словарь частот:')
values = list(set(count.values()))
for values in range(1, len(values) + 1):
    keys = frequency_histogram(values, count)
    print(f'{values} : {keys}')
