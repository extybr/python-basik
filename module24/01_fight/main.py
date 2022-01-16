import random


class Unit:

    def __init__(self, name, health):
        self.health = health
        self.name = name

    def winner(self):
        if self.name == 'Воин-1':
            self.health -= 20
            print('Удар наносит {}. Очки второго: {}'.format(self.name, self.health))
        elif self.name == 'Воин-2':
            self.health -= 20
            print('Удар наносит {}. Очки первого: {}'.format(self.name, self.health))
        # Unit.get_health(self)

    def get_health(self):
        if self.health == 0:
            print('Выиграл {}'.format(self.name))


first = Unit('Воин-1', 100)
second = Unit('Воин-2', 100)
unit = (first, second)
while first.health and second.health != 0:
    win = random.choice(unit)
    win.winner()
    win.get_health()
