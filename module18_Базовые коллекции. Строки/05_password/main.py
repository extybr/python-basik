
while True:
    password = input('Придумайте пароль: ')
    digit = [number for number in password if number.isdigit()]
    three_letters = [letter for letter in password if letter.isupper()]
    # print(digit, three_letters)
    if len(password) < 8 or not three_letters or len(digit) < 3 or not password.isascii():
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

# зачет!
