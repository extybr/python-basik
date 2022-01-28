
def analog_zip(text, elements):
    data = tuple()
    for index in range(min(len(text), len(elements))):
        data += ((text[index], elements[index]),)
        # data = (text[index], elements[index])  # для генерации пар
        # print(data)
    return data


string = 'abcd'
numbers = (10, 20, 30, 40)
new_data = analog_zip(string, numbers)
print(new_data)
# print(tuple(zip(string, numbers))) # для сравнения

# зачет!

