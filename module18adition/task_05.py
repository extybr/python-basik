""" Задача 2. Бабушка

# У одной бабушки, когда та переписывается с внуком, постоянно залипает кнопка пробела. В итоге между словами получаются огромные расстояния. Внук не знает как это поправить в самом телефоне, поэтому обратился к вам за помощью.

# Пользователь вводит строку. Напишите программу, которая преобразовывает в этой строке все идущие подряд пробелы в один и выводит результат на экран. """

text = 'У       нас         пошёл                    снег    ! '
new = text.split()
new_text = ' '.join(new)
print(f'Исправленный текст: {new_text}')
