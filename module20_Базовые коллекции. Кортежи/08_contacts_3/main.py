base = dict()
# base = {
#     ('Сидоров', 'Никита'): 4435, ('Сидорова', 'Алина'): 6634, ('Сидоров', 'Павел'): 5510,
#     ('Петров', 'Николай'): 1150, ('Петрова', 'Алла'): 2244, ('Петров', 'Петр'): 1672
# }

while True:
    print('\nВведите номер действия:')
    print('  1. Добавить контакт')
    choice = int(input('  2. Найти человека\n'))
    if choice == 1:
        surname, name = input('Введите имя и фамилию нового контакта (через пробел): '
                              ).title().split()
        if base.get((surname, name), {}):
            print('Такой человек уже есть в контактах.')
            continue
        telephone = int(input('Введите номер телефона: '))
        base.update({(surname, name): telephone})
        print(f'Текущий словарь контактов: {base}')
    if choice == 2:
        search = input('Введите фамилию для поиска: ').title()
        for key in base.keys():
            if search in key:
                print(key[0], key[1], ':', base[key])
                continue
        else:
            print('Контакт в тел.книге не найден')
            continue

# зачет!
