class Student:
    def __init__(self, surname, group, progress):
        self.surname = surname
        self.group = group
        self.progress = progress

    def info(self):
        print('Имя студента: {}. Номер группы: {}. Оценки: {}. Средний балл: {}'.format(
            self.surname, self.group, self.progress, self.get_average()))

    def get_average(self):
        average = sum(self.progress) / len(self.progress)
        return average

    def create_data(self):
        return {self.surname: self.get_average()}


# data = [['Ivan', 23, [2, 2, 4, 4]], ['Anya', 11, [1, 1, 4, 4]]]
data = []
try:
    for _ in range(10):
        name = input('Введите имя студента: ')
        group = int(input('Номер группы: '))
        balls = []
        for _ in range(5):
            ball = int(input('Успеваемость: '))
            balls.append(ball)
        data.append([name, group, balls])
except ValueError:
    print('Введен Неверный тип данных')
# print(data)

data_filter = dict()
for people in data:
    people = Student(people[0], people[1], people[2])
    people.info()
    data_filter.update(people.create_data())
print('\nОтсортированный список по среднему баллу:')
[print(f'Студент: {key}. Средний балл: {value}') for key, value in sorted(data_filter.items())]
