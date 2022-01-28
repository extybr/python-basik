
# сортируем список по очкам игроков (winner[i][2]) методом пузырька
def find_winner(winner):
    for element in range(len(winner) - 1):
        for item in range(len(winner) - 1 - element):
            if winner[item] > winner[item + 1]:
                winner[item], winner[item + 1] = winner[item + 1], winner[item]


with open('first_tour.txt', 'w') as first_tour:
    first_tour.write('80\nIvanov Serg 80\nSegeev Petr 92\nPetrov Vasiliy 98\nVasiliev Maxim 78')

with open('first_tour.txt', 'r') as first_tour:
    print('Содержимое файла first_tour.txt:\n', first_tour.read())

winners = []
with open('first_tour.txt', 'r') as first_tour:
    for number, line in enumerate(first_tour):
        if number == 0:
            winner_points = line
        elif number > 0:
            for word in line.split():
                if str(word).isdigit():
                    if word > winner_points:
                        winners.append(line.split())
# print(winners)

with open('second_tour.txt', 'w') as second_tour:
    second_tour.write(str(winner_points))
    find_winner(winners)    # возвращаем отсортированный список
    for index in range(1, len(winners)):
        for items in winners:
            second_tour.write(f'{index}) {items[1][:1]}. {items[0]}  {items[2]}\n')

with open('second_tour.txt', 'r') as second_tour:
    print('\nСодержимое файла second_tour.txt:\n', second_tour.read())
