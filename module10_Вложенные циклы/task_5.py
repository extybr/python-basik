print('Задача 5. Простые числа')

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.

count = 0
prime = True
numbers = int(input('Введите кол-во цифр: '))
for queue in range(1, numbers + 1):
    number = int(input('Введите ' + str(queue) + ' число: '))
    for divider in range(2, number):
        if number % divider == 0:
            prime = False
    if prime:
        count += 1
print('Кол-во простых чисел в последовательности: ', count)
