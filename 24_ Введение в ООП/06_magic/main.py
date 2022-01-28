class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Water):
            return Steam()

    def __str__(self):
        return 'Огонь'


class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()

    def __str__(self):
        return 'Земля'


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Dirt()

    def __str__(self):
        return 'Вода'


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return 'Воздух'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Lightning:
    def __str__(self):
        return 'Молния'


class Lava:
    def __str__(self):
        return 'Лава'


class Dust:
    def __str__(self):
        return 'Пыль'


water = Water()
earth = Earth()
fire = Fire()
air = Air()
print(water + air)
print(fire + air)
print(earth + air)
print(air)

