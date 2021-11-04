print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”,
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
#
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
#
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

text = input('Введите строку: ')
count = 0
maximum = 0
for word in text:
    if word == 's':
        count += 1
    elif word != 's':
        count = 0
    if maximum < count:
        maximum = count
print('Самая длинная последовательность: ', maximum)