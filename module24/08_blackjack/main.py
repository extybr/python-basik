import random


class BlackJack:
    cards = {
        2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Валет': 10, 'Дама': 10,
        'Король': 10, 'Туз': 11
    }
    summa = 0

    def output(self, key):
        value = self.cards[key]
        self.summa += int(value)
        print(self.summa)


player = BlackJack()
manager = BlackJack()
while True:
    if player.summa > 21:
        print('Игрок проиграл')
        break
    elif player.summa == 21:
        print('Игрок выиграл')
        break
    elif manager.summa > 21:
        print('Крупье проиграл')
        break
    elif manager.summa == 21:
        print('Крупье выиграл')
        break
    choice = input('Продолжить игру (нажать: любую клавишу) или пасc (нажать: 0) ? ')
    if choice != '0':
        print('Игрок берет карту')
        card_player = random.choice([keys for keys in player.cards.keys()])
        player.output(card_player)
    print('Крупье берет карту')
    card_manager = random.choice([keys for keys in manager.cards.keys()])
    manager.output(card_manager)
