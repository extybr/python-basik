
def create_numbers(number, new):
    for item in number:
        if isinstance(item, list):
            create_numbers(item, new)
        else:
            new.append(item)
    return new


numbers = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
# numbers = ['1', '5', ['3', ['14', '15']]]
new_numbers = []
result = create_numbers(numbers, new_numbers)
print('Ответ:', result)

# зачет!
