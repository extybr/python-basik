

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

with open("../05_text_calc/calc.txt", "r", encoding="utf-8") as calc:
    with open("calc.txt", "w", encoding="utf-8") as new_calc:
        for row, line in enumerate(calc, 1):
            try:
                operation = line.split()[1]
                # for item in operation:
                if (operation[0] or operation[1]) in calculator.keys() and len(
                        operation) > 1 and operation != '//' and operation != '**':
                    # print(operation, row)
                    print(f'Обнаружена ошибка в строке {row}: {line} ')
                    choice = input(' Хотите исправить? да/нет : ')
                    if choice == 'да'.lower():
                        out = input('Введите исправленную строку: ')
                        new_calc.write(f'{out}\n')
                    else:
                        new_calc.write(line)
                else:
                    new_calc.write(line)
            except IndexError:
                print('Возможно, строка пустая')

summa = 0
with open("calc.txt", "r", encoding="utf-8") as new_calc:
    try:
        for line in new_calc:
            first = line.split()[0]
            operation = line.split()[1]
            second = line.split()[2]
            try:
                action = calculate(operation, calculator)
                result = action(int(first), int(second))
                if isinstance(result, int) or isinstance(result, float):
                    summa += float(result)
            except ZeroDivisionError:
                print("Делить на ноль нельзя!")
    except ValueError:
        print("Число должно быть целым (integer)")
    except IndexError:
        print('Возможно, строка пустая')
print('Результат:', summa)

