
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


def extract_tag(site_code, tag, my_depth):
    for key, value in site_code.items():
        if tag in key or my_depth == 1:
            # return print(f'Значение ключа: {site_code[tag]}')
            return print(f'Значение ключа: {site_code.get(tag)}')
        if isinstance(value, dict):
            extract_tag(value, tag, my_depth - 1)


my_key = input('Введите искомый ключ: ')
choice = input('Хотите ввести максимальную глубину? Y/N: ').upper()

if choice == 'Y':
    depth = int(input('Введите максимальную глубину: '))
    extract_tag(site, my_key, depth)
elif choice == 'N':
    extract_tag(site, my_key, 0)
