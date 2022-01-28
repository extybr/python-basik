""" Задача 2. Игроки

Есть готовый словарь игроков, у каждого игрока есть имя, команда,
в которой он играет, а также его текущий статус, в котором указано,
отдыхает он, тренируется или путешествует:

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
} 
Напишите программу, которая выводит на экран вот такие данные в разных строчках:
    Все члены команды из команды А, которые отдыхают.
    Все члены команды из группы B, которые тренируются.
    Все члены команды из команды C, которые путешествуют. """

def find_member(team, status):
    new = list()
    for people in players_dict:
        if players_dict.get(people).get('team') == team and players_dict.get(people).get(
                'status') == status:
            new.append(players_dict[people]['name'])
    return new


players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

member_a = find_member("A", 'Rest')
member_b = find_member("B", 'Training')
member_c = find_member("C", 'Travel')
print('Все члены команды из команды А, которые отдыхают:', member_a)
print('Все члены команды из группы B, которые тренируются:', member_b)
print('Все члены команды из команды C, которые путешествуют:', member_c)
