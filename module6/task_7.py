print('Задача 7. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин

hour = 1
all_work = 0
all_wife = False
print('Начался 8-часовой рабочий день')
while hour != 4:
    print(hour, 'час')
    hour += 1
    work = int(input('Сколько задач решит Максим? '))
    all_work += work
    wife = int(input('Звонит жена. Взять трубку? (1-да, 0-нет) '))
    if bool(wife) == 1:
        all_wife = True
print('Рабочий день закончился. Всего выполнено задач: ', all_work)
if all_wife:
    print('Нужно зайти в магазин')
elif not all_wife:
    print('В магазин можно не ходить')
