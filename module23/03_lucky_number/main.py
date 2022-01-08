import random

summa = 0
while summa < 777:
    out_file = open('out_file.txt', 'a')
    try:
        number = int(input('Введите число: '))
        summa += number
        out_file.write(str(f'{number}\n'))
        lucky = random.randint(1, 13)
        if lucky == 13:
            print('Вас постигла неудача!')
            break
    except ValueError:
        print('Необходимо целое число!')
    finally:
        out_file.close()
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
