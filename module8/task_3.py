print('Задача 3. Это будет бомба')

# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
#
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва..
#
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.

sec = int(input('Через сколько секунд должна взорваться бомба? '))
for number in range(sec, 0, -1):
    print('До взрыва осталось: ', number)
    answer = int(input('Хочет ли он обезвредить бомбу сейчас? 0-нет/1-да '))
    if answer == 1:
        print('Бомба обезврежена! До взрыва оставалось ', number, ' секунд')
        break
    elif number == 1:
        print('Бомба взорвалась!')
        break
