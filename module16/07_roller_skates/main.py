
my_skates = []
skates = int(input('Кол-во коньков: '))
for index in range(1, skates + 1):
    size = int(input(f'Размер {index} пары: '))
    my_skates.append(size)

my_people = []
people = int(input('\nКол-во людей: '))
for index in range(1, people + 1):
    foot = int(input(f'Размер ноги {index} человека: '))
    my_people.append(foot)

my_skates = list(set(my_skates))
my_people = list(set(my_people))
count = 0
for index in my_skates:
    if index in my_people:
        count += 1
print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {count}')

# зачет!

