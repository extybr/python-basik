print('Задача 4. Урок информатики 3')

# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».
 
# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

number = input('Введите экспоненциальное число: ')
print('Мантисса: ', end = '')
for symbol in number:
    if symbol != 'e':
        print(symbol, end = '')
    elif 'e' in symbol:
        print(' ', end='\nПорядок числа: ')
