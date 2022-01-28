violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

numbers = int(input('Сколько песен выбрать? '))
sounds = 0
for songs in range(1, numbers + 1):
    title = input(f'Название {songs} песни: ')
    while title not in violator_songs.keys():
        print('Такой песни в списке нет.')
        title = input(f'Название {songs} песни: ')
    sounds += round(violator_songs[title], 2)
print(f'Общее время звучания песен: {sounds} минут')
