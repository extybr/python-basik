
def items_sort(my_scoreboard, step):
    for run in range(step):
        index = 0
        while index < len(my_scoreboard) - 1:
            temp = my_scoreboard[index]
            my_scoreboard[index] = my_scoreboard[index - 1]
            my_scoreboard[index - 1] = temp
            index += 1
    return my_scoreboard


number = int(input('Сколько элементов в списке: '))
scoreboard = []
for items in range(1, number + 1):
    my_items = input(f'Введите {items}-й элемент: ')
    scoreboard.append(my_items)

shift = int(input('Сдвиг: '))
print(f'Изначальный список: {scoreboard}')
new_scoreboard = items_sort(scoreboard, shift)
print(f'Сдвинутый список: {new_scoreboard}')

# зачет!
