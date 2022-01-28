
def defining_integers(address):
    for index in address:
        if len(address) != 4 or ',' in index:
            return print('Адрес - это четыре числа, разделенные точками')
        elif not index.isdigit():
            return print(f'{index}- не целое число')
        elif int(index) > 255 or int(index) < 0:
            return print('Число IP адреса должно быть в диапазоне от 0 до 255')
    else:
        return print('IP-адрес корректен')


ip_address = input('Введите IP: ').split('.')
# print(ip_address)
defining_integers(ip_address)

# зачет!

