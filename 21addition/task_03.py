""" Задача 3. Поиск элемента

Когда мы работаем с большой многоуровневой структурой,
нам нередко необходимо пройтись по ней и найти нужный
элемент. Для этого в программировании используются 
специальные алгоритмы поиска.

Напишите функцию, которая находит заданный пользователем
ключ в словаре и выдаёт значение этого ключа на экран.
В качестве примера можно использовать такой словарь:  """

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(www, tag):
    if www.get(tag, {}):
        return www[tag]
    for value in www.values():
        if isinstance(value, dict):
            result = search(value, tag)
            if result:
                break
    else:
        result = None
    return result



search_key = input('Искомый ключ: ')
values = search(site, search_key)
if values:
    print(f'Значение: {values}')
else:
    print('Такого ключа в структуре сайта нет.')
