
def bubble_sort(my_warehouse):
    for run in range(len(my_warehouse) - 1):
        for index in range(len(my_warehouse) - 1 - run):
            if my_warehouse[index] > my_warehouse[index + 1]:
                my_warehouse[index], my_warehouse[index + 1] = my_warehouse[index + 1], my_warehouse[index]
    return my_warehouse


number = int(input('Кол-во контейнеров: '))
warehouse = []
for _ in range(number):
    weight = int(input('Введите вес контейнера: '))
    while weight > 200:
        print('Вес контейнера не должен превышать 200 кг')
        weight = int(input('Введите вес контейнера: '))
    warehouse.append(weight)
# print(warehouse)

new_weight = int(input('\nВведите вес нового контейнера: '))
warehouse.append(new_weight)
new_warehouse = bubble_sort(warehouse)
# print(new_warehouse)

count = 0
for my_item in new_warehouse:
    count += 1
    if my_item == new_weight:
        break

double = 0
for my_item in new_warehouse:
    if my_item == new_weight:
        double += 1

new_count = count + double - 1
print('\nНомер, куда встанет новый контейнер:', new_count)

# зачет!
