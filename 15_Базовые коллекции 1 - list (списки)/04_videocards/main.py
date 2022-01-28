
numbers = int(input('Кол-во видеокарт: '))
temp_card = 0
old_item = []
for index in range(1, numbers + 1):
    card = int(input(f'{index} Видеокарта: '))
    old_item.append(card)
    if temp_card < card:
        temp_card = card

print(f'Старый список видеокарт: {old_item}')

new_item = []
for video_card in old_item:
    if video_card != temp_card:
        new_item.append(video_card)

print(f'Новый список видеокарт: {new_item}')

# зачет!
