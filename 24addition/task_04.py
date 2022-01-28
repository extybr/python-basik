""" Задача 2. Семья

Реализуйте класс «Семья», который состоит из атрибутов «Имя»,
Деньги» и «Наличие дома» и объекты которого могут выполнять
следующие действия:
    Отобразить информацию о себе.
    Заработать денег (подаётся число, которое прибавляется
	к текущему значению денег).
    Купить дом (подаётся стоимость дома и необязательный
	аргумент «Скидка»). Вывести соответствующее сообщение
	об успешной/неуспешной покупке дома.
Создайте как минимум один экземпляр класса и проверьте
работу методов. """

class Family:
    surname = 'Common family'
    money = 1200
    have_house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
                self.surname, self.money, self.have_house))

    def buy_house(self, house_price):
        if self.money >= house_price:
            self.money -= house_price
            self.have_house = True
            print(f'Дом куплен. Остаток на счете: {self.money} евро\n')
        else:
            money = self.money - house_price
            print(f'На покупку дома не хватает {abs(money)} евро\n')


my_family = Family()
my_family.info()
my_family.buy_house(10000)
my_family.info()
