
def get_country(all_world, city):
    for key, values in all_world.items():
        for _ in values:
            if city in values:
                return print(f'Город {city} расположен в стране {key}.')
    else:
        print(f'По городу {city} данных нет.')


# countries = 2
# world = {
#     'Россия': ['Москва', 'Новгород', 'Петербург'],
#     'Германия': ['Берлин', 'Лейпциг', 'Мюнхен']
# }

countries = int(input('Кол-во стран: '))
world = dict()
for index in range(1, countries + 1):
    country = dict()
    towns = input(f'{index} страна: ')
    town = towns.split()
    country[town[0]] = town[1:]
    world.update(country)

for index in range(1, countries + 1):
    my_town = input(f'\n{index} город: ')
    get_country(world, my_town)
