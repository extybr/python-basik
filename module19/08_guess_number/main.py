
maximum = int(input('Введите максимальное число: '))
numbers = set(range(maximum + 1))

while True:
    choice = input('Нужное число есть среди вот этих чисел: ')
    if choice == 'Помогите!':
        print(f'Артём мог загадать следующие числа: {numbers}')
        break
    guess = set([int(number) for number in set(choice.split())])
    print(guess)
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        numbers = guess
        print(numbers)
    elif answer == 'Нет':
        numbers.difference_update(guess)
        print(numbers)
    if len(guess) == 1 and answer == 'Да':
        print('Угадал!')
        break
