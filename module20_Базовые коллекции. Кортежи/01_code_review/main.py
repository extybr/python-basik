students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def search_data(data):
    age, interests = [], []
    count = 0
    for item in data:
        age.append((item, students[item]['age']))
        interests += (data[item]['interests'])
        count += len(data[item]['surname'])
    return set(interests), count, age


full_interests, total_length, pairs = search_data(students)
print(f'Список пар "ID студента - Возраст": {pairs}')
print(f'Полный список интересов всех студентов: {full_interests}')
print(f'Общая длина всех фамилий студентов: {total_length}')

# зачет!
