
name = input('Введите ваше имя: ')

choice = int(input(
    'Хотите посмотреть чат? (нажмите: 1) или Начать переписку в нем? (нажмите: 2)  '))
if choice == 1:
    with open('chat.txt', 'r', encoding='utf-8') as chat:
        print(chat.read())
elif choice == 2:
    print('Для завершения и выхода из чата: (введите: 3) ')
    while True:
        message = input('Введите сообщение: ')
        if message == '3':
            break
        with open('chat.txt', 'a', encoding='utf-8') as chat:
            chat.write(f'{name}: {message}\n')
        with open('chat.txt', 'r', encoding='utf-8') as chat:
            print(chat.read())

# pyinstaller -F --icon=favicon.ico main.py
