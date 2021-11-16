
def bubble_sort(my_sorting):
    for run in range(len(my_sorting) - 1):
        for index in range(len(my_sorting) - 1 - run):
            if my_sorting[index] > my_sorting[index + 1]:
                my_sorting[index], my_sorting[index + 1] = my_sorting[index + 1], my_sorting[index]
    return my_sorting


number = int(input('Сколько элементов будет в списке: '))
sorting = []
for my_index in range(1, number + 1):
    items = int(input(f'Введите {my_index}-й элемент списка: '))
    sorting.append(items)

print(f'\nИзначальный список: {sorting}')

sorting = bubble_sort(sorting)
print(f'\nОтсортированный список: {sorting}')

# зачет!
