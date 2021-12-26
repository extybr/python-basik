site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def change_model(original_site, new_model):
    new_site = original_site
    for key, value in new_site.items():
        if 'телефон' in value:
            new_site[key] = f'Куплю/продам {new_model} недорого'
        if 'iphone' in value:
            new_site[key] = f'У нас самая низкая цена на {new_model}'
        if isinstance(value, dict):
            change_model(value, new_model)
    return new_site


number = int(input('Сколько сайтов: '))
for _ in range(number):
    model = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {model}: ')
    result = change_model(site, model)
    print(result)

# зачет!
