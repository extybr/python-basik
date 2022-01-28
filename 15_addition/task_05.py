""" # Задача 2. Кратность

# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K. """

numbers = int(input('Кол-во чисел в списке: '))
nums_list = []
for i in range(1, numbers + 1):
    number = int(input('Введите ' + str(i) + ' число: '))
    nums_list.append(number)
print(nums_list, '\n******')

divider = int(input('Введите делитель: '))
summa = 0
for j in nums_list:
    if j % divider == 0:
        result = j // divider        
        print(f'Индекс числа {j}: {result}')
        summa += j

print(f'Сумма индексов: {summa}')
