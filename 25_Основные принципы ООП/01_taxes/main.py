class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self, *args):
        return sum([*args])


class Appartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


money = float(input('Кол-во денег на счету: '))
worth_appartment = float(input('Стоимость квартиры: '))
worth_car = float(input('Стоимость машины: '))
worth_country_house = float(input('Стоимость дачи: '))
appartment = Appartment(worth_appartment)
car = Car(worth_car)
country_house = CountryHouse(worth_country_house)
my_property = Property(money)
tax_property = my_property.tax_calculation(
    appartment.tax_calculation(), car.tax_calculation(), country_house.tax_calculation())
print('Налог на имущество:', tax_property)
if money < tax_property:
    tax = tax_property - money
    print(f'Для уплаты налогов вам не хватает {tax} y.e')
