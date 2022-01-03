import os
import zipfile
from tabulate import tabulate


def letters_sorted(numbers_sort):
    new = dict()
    numbers_value = sorted(numbers_sort.values(), reverse=True)
    for items in numbers_value:
        for keys, values in numbers_sort.items():
            if items == numbers_sort[keys]:
                new[keys] = items
    return new


zip_file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
info_file = zip_file.namelist()
for file in info_file:
    zip_file.extract(file)
zip_file.close()
# print(info_file)

file_name = ''
for files in os.walk(os.getcwd()):
    for names in files:
        for name in names:
            # if name.endswith('.txt'):
            if name in info_file:
                file_name = name

alphabet = (
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'абвгдеёжзийклмнопрстуфхцчшщыъьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЬЭЮЯ')

numbers = dict()
with open(file_name, 'r', encoding='utf-8') as text:
    for line in text.readlines():
        for letter in line:
            if letter in alphabet:
                if letter not in numbers:
                    numbers[letter] = 0
                numbers[letter] += 1

new_numbers = letters_sorted(numbers)

table = []
for key, value in new_numbers.items():
    table.append([key, value])
print(tabulate(table, headers=['Буква', 'Частота'], tablefmt='psql'))
