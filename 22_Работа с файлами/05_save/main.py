import os


text = input('Введите строку: ')
# text = 'test-test'

path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
path = path.replace(' ', '\\')
if path.find('C:') == -1:
    path = 'C:\\' + path
# print(path)

name = input('Введите имя файла: ')
# name = 'my_document.txt'
print(os.path.join(path, name))

if os.path.exists(os.path.join(path, name)):
    choice = input('Вы действительно хотите перезаписать файл? <да/нет>: ')
    if choice == 'да'.lower():
        with open(os.path.join(path, name), 'w') as file:
            file.write(text)
        print('Файл успешно перезаписан!')
    else:
        print('Отмена перезаписи')
else:
    with open(os.path.join(path, name), 'w') as file:
        file.write(text)
    print('Файл успешно сохранён!')
file = open(os.path.join(path, name), 'r')
file_read = file.read()
print('Содержимое файла:', file_read)
file.close()
