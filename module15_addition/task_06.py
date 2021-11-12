""" # Задача 3. Собачьи бега

# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.

# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке. """

numbers = int(input('Введите количество собак: '))
scores = []
balls = int(input('Введите кол-во баллов у каждой собаки: '))
for i in range(1, numbers + 1):
    for j in range(balls):
        score = int(input(f'Введите набранный бал {i} собаки: '))
        scores.append(score)
    print(f'\nБаллы {i} собаки = {scores}\n')

    maxi_mini = 0
    for k in scores:
        if maxi_mini < k:
            maxi_mini = k
    scores.append(maxi_mini)
    print(scores)
    print()
    scores = []


""" maxi_mini = ''
    for k in scores:
        maxi_mini += str(k)
    print(maxi_mini, end='') """