""" Задача 1. Заказ

#  После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение с его именем и номером заказа.

#  Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение. Для решения используйте строковый метод format. """

name = input('Имя: ')
number = int(input('Номер заказа: '))
print(f'Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!')
