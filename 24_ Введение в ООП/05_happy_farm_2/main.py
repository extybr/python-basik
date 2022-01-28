class Potato:
    states = {0: 'отсутствует', 1: 'росток', 2: 'зеленая', 3: 'зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.count = count
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела\n')
        else:
            print('Картошка созрела. Можно собирать.')


class Gardener:
    def __init__(self, name):
        self.name = name
        self.have_plant = False
        self.basket = []

    def __str__(self):
        return 'Садовник ухаживает за грядкой'

    def harvest(self):
        print('\nСадовник собирает урожай')
        self.have_plant = True
        self.basket.append(my_garden.count)
        print('Урожай собран:', self.have_plant, '\nСобранный урожай:', self.basket)


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
worker = Gardener('Andrey')
for _ in range(3):
    print(worker)
    my_garden.grow_all()
    my_garden.are_all_ripe()
worker.harvest()

my_garden = PotatoGarden(7)
worker.harvest()
