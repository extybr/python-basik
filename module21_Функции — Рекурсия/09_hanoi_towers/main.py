
def move_tower(height, from_pole, to_pole, with_pole):
    if height > 0:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole, height)
        move_tower(height - 1, with_pole, from_pole, to_pole)


def move_disk(first, second, pole):
    print(f'Переложить диск {pole} со стержня номер {first} на стержень номер {second}')


number = int(input('Введите количество дисков: '))
move_tower(number, '1', '2', '3')

# зачет!
