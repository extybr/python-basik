
numbers = int(input('Кол-во человек: '))
people = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {people} человек')

my_people = list(range(1, numbers + 1))

count = 0
for _ in range(numbers - 1):
    print(f'\nТекущий круг людей: {my_people}')
    start_count = count % len(my_people)
    count = (start_count + people - 1) % len(my_people)
    print(f'Начало счёта с номера {my_people[start_count]}')
    print(f'Выбывает человек под номером {my_people[count]}')
    my_people.remove(my_people[count])
print(f'\nОстался человек под номером {my_people[0]}')

# зачет!

