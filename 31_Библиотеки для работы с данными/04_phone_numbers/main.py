import re

numbers = ['9999999999', '999999-999', '99999x9999']
regex = r'\b[89]\d{9}\b'
pattern = re.compile(regex)
for item, number in enumerate(numbers):
    if pattern.findall(number):
        print(f'{item + 1}-й номер ({number}): всё в порядке')
    else:
        print(f'{item + 1}-й номер ({number}): не подходит')
