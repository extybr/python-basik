""" Задача 3. Универсальная программа

Один заказчик попросил нас написать небольшой
скрипт для своих криптографических нужд. При
этом он заранее предупредил, что скрипт должен
уметь работать с любым итерируемым типом данных.

Напишите функцию, которая возвращает список 
из элементов итерируемого объекта (кортежа, 
строки, списка, словаря), у которых индекс чётный. """

text = 'О Дивный Новый мир!'
new = list()
[new.append(b) for a, b in enumerate(text) if a % 2 == 0]
print(f'Результат: {new}')
lst = [100, 200, 300, 'буква', 0, 2, 'а']
new = list()
[new.append(b) for a, b in enumerate(lst) if a % 2 == 0]
print(f'Результат: {new}')

