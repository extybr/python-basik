
class Game:
    """ Вас приветствует упрощенная игра крестики-нолики """
    text = """ 
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    ------------- 
    """

    def replace_number(self, symbol):
        while self.text.find(str(symbol)) != -1:
            number = input('Введите цифру, куда поставить крестик <X>: ')
            self.text = self.text.replace(number, 'X')
            print(self.text)
            number = input('Введите цифру, куда поставить крестик <0>: ')
            self.text = self.text.replace(number, '0')
            print(self.text)


gamer = Game()
numbers = list(range(1, 10))
print(gamer.__doc__)
for my_number in numbers:
    gamer.replace_number(my_number)
print('Игра закончена')
