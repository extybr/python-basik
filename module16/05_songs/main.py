
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

number = int(input('Сколько песен выбрать? '))
all_time_songs = 0

for index in range(1, number + 1):
    my_song = input(f'Название {index} песни: ')
    for song, duration in violator_songs:
        if my_song == song:
            all_time_songs += duration

print(f'Общее время звучания песен: {all_time_songs}')

# зачет!

