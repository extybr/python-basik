""" Задача 3. Пакеты

#  При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации. Их количество равно N. Допустим, каждый пакет содержит четыре числа, каждое из которых равно нулю или единице. Эти числа называются битами. Иногда в кодировке сообщения встречаются ошибки, и в пакете эта ошибка обозначается числом -1. Если таких ошибок не больше одной, то этот пакет мы целиком добавляем в список для декодирования, а иначе отбрасываем. 

#  Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран итоговое сообщение для декодирования, а также количество ошибок в нём и количество необработанных пакетов. """

packet = int(input('Кол-во пакетов: '))
my_bit = []
my_packet =[]
bad_count = 0
for index in range(1, packet + 1):
    print(f'Пакет номер {index}')
    for j in range(1, 5):
        bit = int(input(f'{j} бит: '))
        my_bit.append(bit)
    if my_bit.count(-1) <= 1:
        my_packet.extend(my_bit)           
    else:
        print('Много ошибок в пакете.')
        bad_count += 1
    my_bit = []    
print(f'Полученное сообщение: {my_packet}')
print(f'Кол-во ошибок в сообщении: {bad_count}')