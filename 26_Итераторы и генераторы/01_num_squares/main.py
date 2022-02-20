from collections.abc import Iterable


class SquareNumber:
    def __init__(self, number: int) -> None:
        self.number = number
        self.count = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> Iterable[int]:
        if self.count < self.number:
            self.count += 1
            return self.count ** 2
        raise StopIteration


def number_gen(number: int) -> Iterable[int]:
    for i in range(1, number + 1):
        yield i ** 2


my_number = int(input('Введите число: '))

numbers = SquareNumber(my_number)
for _ in range(my_number):
    print(next(numbers))

for element in number_gen(my_number):
    print(element)

generator = (item ** 2 for item in range(1, my_number + 1))
[print(square) for square in generator]


