print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

summa = 0
complect_ticket = 0
end_ticket = int(input('Введите число карточек: '))
for ticket in range(1, end_ticket):
    my_ticket = int(input('Введите номер карточки: '))
    summa += my_ticket
    complect_ticket += ticket
lost_ticket = complect_ticket - summa + end_ticket
print('номер потерянной карточки', lost_ticket)
