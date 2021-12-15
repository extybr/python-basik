""" Задача 1. Член семьи

Дана структура, которая содержит описание одного из членов семьи
(имя, фамилия, хобби, сколько лет и дети):

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

Напишите программу, которая реализует такую структуру:
имя, фамилия, хобби, кол-во лет и дети. Затем, с помощью метода get
и установки значения по умолчанию, проверьте есть ли ребёнок с именем
Bob. Затем в отдельную переменную получите фамилию этого ребёнка
и выведите её на экран. Если у него нет фамилии, то получите значение ‘Nosurname’. """

family_member = dict()
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
family_member.update()
family_member = {"name": name, "surname": surname}
hobbies = input('Введите хоби: ').split()
family_member['hobbies'] = hobbies
family_member.update()
age = int(input('Введите возраст: '))
family_member["age"] = age
children = []
numbers = int(input('Кол-во детей: '))
for child in range(numbers):
    children_name = input('Введите имя ребенка: ')
    children_age = int(input('Введите возраст ребенка: '))
    children.append({"name": children_name, "age": children_age})

family_member['children'] = children
family_member.update()
print(family_member)
find_name = input('Введите искомое имя ребенка: ')
for items in family_member["children"]:
    if find_name in items['name']:
        if items.get('surname'):
            print(items['surname'])
        else:
            print(f'Ребенок с именем {find_name} существует')
        break
else:
    print(f'Ребенок с именем {find_name} не существует')
    

