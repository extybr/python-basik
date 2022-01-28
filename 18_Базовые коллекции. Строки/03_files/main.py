
file = input('Название файла: ')
special_character = '@№$%^&*()'
file_extension = ('.txt', '.docx')
if file[0] in special_character:
    print('Ошибка: название начинается на один из специальных символов')
if not (file.endswith(file_extension[0]) or file.endswith(file_extension[1])):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
elif special_character.find(file[0]) == -1:
    print('Файл назван верно.')

# зачет!
