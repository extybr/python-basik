from typing import Callable, Any


def how_are_you(function: Callable) -> Callable:
    def wrapped_function(*args) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = function(*args)
        return result
    return wrapped_function


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def calculate(number: int) -> int:
    return pow(number, 100)


test()
print(calculate(25))

