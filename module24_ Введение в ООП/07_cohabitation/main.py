import random


class Human:
    degree_satiety = 50
    food = 50
    money = 0

    def __init__(self, name):
        self.name = name

    def eat(self):
        self.degree_satiety += 10
        self.food -= 10

    def work(self):
        self.degree_satiety -= 10
        self.money += 10

    def play(self):
        self.degree_satiety -= 10

    def shopping(self):
        self.food += 10
        self.money -= 10

    def __add__(self, other):
        pass


man = Human('Артём')
woman = Human('Girl')
people = (man, woman)
for day in range(1, 365):
    print('День {}:'.format(day))
    for human in people:
        number_cube = random.randint(1, 6)
        if human.degree_satiety <= 0:
            print('{} умер от голода'.format(human.name))
            break
        elif 0 < human.degree_satiety < 20:
            human.eat()
        elif human.food < 10:
            human.shopping()
        elif human.money < 50:
            human.work()
        elif number_cube == 1:
            human.work()
        elif number_cube == 2:
            human.eat()
        else:
            human.play()
    print('Сытость {} {}'.format(man.name, man.degree_satiety))
    print('Деньги {}'.format(man.money))
    print('Еда {}\n'.format(man.food))
    print('Сытость {} {}'.format(woman.name, woman.degree_satiety))
    print('Деньги {}'.format(woman.money))
    print('Еда {}\n'.format(woman.food))
