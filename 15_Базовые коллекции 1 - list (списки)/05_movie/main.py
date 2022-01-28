films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

number = int(input('Сколько фильмов хотите добавить? '))
favorite = []
for index in range(number):
    my_film = input('Введите название фильма: ')
    for _ in films:
        if my_film in favorite:
            print('Фильм уже есть в вашем списке.')
            break
        if my_film in films:
            favorite.append(my_film)
            break
        else:
            print('Ошибка. Данного фильма нет в списке.')
            break

print(favorite)

# зачет!
