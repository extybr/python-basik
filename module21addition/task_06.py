""" Задача 3. Помощь другу

Нашего друга попросили написать функцию, которая на вход принимает
 список всякого мусора. Ему нужно подготовить из этого списка список 
 словарей, чтобы его коллеги смогли дальше продолжить обработку данных.
  Вот список правил, что нужно сделать с изначальным списком:

Если в списке встретился словарь, то оставляем его.
Если в списке встретилась строка, то из неё нужно сделать словарь
 и положить его в итоговый список, например  “abc” → {“abc”: “abc”}.
С числами нужно сделать то же самое, что и со строками.
Всё остальное выкидываем из нашего списка.

Друг написал программу, но в ней ошибка, так как она что-то не то
 выводит :( Нужна ваша помощь, вот сама программа: 
 Исправьте программу и убедитесь, что всё работает верно. """

def create_dict(element, template):
    if isinstance(element, dict):
        return element
    if isinstance(element, int) or isinstance(element, float) or isinstance(element, str):
        template[element] = element
        return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element, template=dict()))
    for _ in new_list:
        if None in new_list:
            new_list.remove(None)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)
