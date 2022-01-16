import random


class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info(self):
        print('Имя: {}. Возраст: {}. Дети: {}.'.format(
            self.name, self.age, str(', ').join(self.children)))

    def soothe_child(self):
        print('Отец идет успокоить')

    def feed_child(self):
        print('Отец идет накормить')


class Child:
    def __init__(self, name, age, state_calm, state_hunger):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def info(self):
        print('Имя: {}. Возраст: {}. Состояние спокойствия: {}. Состояние голода: {}.'.format(
            self.name, self.age, self.state_calm, self.state_hunger))
        if self.state_calm:
            Parent.soothe_child(self.state_calm)
        if self.state_hunger:
            Parent.feed_child(self.state_hunger)


baby = {'Sonya': 3, 'Misha': 5, 'Masha': 6}
father = Parent('Vladislav Petrov', 40, baby)
father.info()
state = (False, True)
for names, ages in baby.items():
    information = Child(names, ages, random.choice(state), random.choice(state))
    information.info()

