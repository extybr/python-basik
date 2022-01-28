""" Задача 2. Всё в одном

Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком
в другой город, и там у него случилась беда: его диск пришлось
отформатировать, а доступ в интернет отсутствует. Остался только
телефон с мобильным интернетом. Так как со связью (и с памятью)
проблемы, друг попросил вас скинуть одним файлом все решения и 
скрипты, которые у вас сейчас есть. """

file_01 = open('001.txt', 'r', encoding='utf-8')
file_02 = open('002.py', 'r', encoding='utf-8')
new = open('new.txt', 'a')
new_file = []
for i in file_01:
    new_file.append(i)
new.write('\n')
new.write('\n'.join(new_file))
new.write('*' * 50)
new.write('*' * 50)
new.write('\n')
file_01.close()
for i in file_02:
    new_file.append(i)
new.write('\n')
new.write('\n'.join(new_file))
new.write('*' * 50)
new.write('\n')
file_02.close()
new.close()
new_read = open('new.txt', 'r')
for j in new_read:
