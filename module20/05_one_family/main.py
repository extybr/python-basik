
base = {
    ('Сидоров', 'Никита'): 35, ('Сидорова', 'Алина'): 34, ('Сидоров', 'Павел'): 10,
    ('Петров', 'Николай'): 50, ('Петрова', 'Алла'): 44, ('Петров', 'Петр'): 12
}

surname = input('Введите фамилию: ').title()
# surname = 'Петрова'
for family in base:
    if (surname in family[0][:-1]) or (surname in family[0]) or (surname[:-1] in family[0]):
        print(family[0], family[1], base[family])

# зачет!

