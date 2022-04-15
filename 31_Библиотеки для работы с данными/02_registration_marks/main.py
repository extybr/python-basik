import re

numbers = 'А578ВЕ777, ОР233787, К901МН666, СТ46599, СНИ2929П777, 666АМР666'

automobile = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', numbers)
print('Список номеров частных автомобилей:', automobile)
taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', numbers)
print('Список номеров такси:', taxi)
