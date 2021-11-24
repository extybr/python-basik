
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    number = len(guests)
    print(f'Сейчас на вечеринке {number} человек: {guests}')
    choice = input('Гость пришел или ушел? ').lower()
    name = input('Имя гостя: ').title()
    if choice == 'пришел' and number < 6:
        print(f'Привет, {name}!')
        guests.append(name)
    elif choice == 'пришел' and number >= 6:
        print(f'Прости, {name}, но мест нет.')
    elif choice == 'ушел':
        if name not in guests:
            print('Гость на вечеринке отсутствует')
            continue
        print(f'Пока, {name}!')
        guests.remove(name)
    elif choice or name == 'Пора спать':
        break

# зачет!
