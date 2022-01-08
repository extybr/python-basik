
def calculate(match, dictionary, default="Данная функция в калькуляторе отсутствует"):
    for key in dictionary.keys():
        if match == key:
            return dictionary[key]
    return lambda *x: default


calculator = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "**": lambda x, y: x ** y,
    "//": lambda x, y: x // y,
    "%": lambda x, y: x % y,
    "*": lambda x, y: x * y
}

summa = 0
with open("calc.txt", "r", encoding="utf-8") as calc:
    for line in calc:
        try:
            first = line.split()[0]
            operation = line.split()[1]
            second = line.split()[2]
            try:
                action = calculate(operation, calculator)
                result = action(int(first), int(second))
                # print(result)
                if isinstance(result, int) or isinstance(result, float):
                    summa += float(result)
            except ZeroDivisionError:
                print("Делить на ноль нельзя!")
            except ValueError:
                print("Число должно быть целым (integer)")
        except IndexError:
            print('Возможно, строка пустая')
print('Результат:', summa)
