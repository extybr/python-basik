# Меняем местами первый и последний элемент списка

def change(lst):
    new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
    new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
    lst.append(new_end)  # Добавляем к списку новый последний элемент
    lst.insert(0, new_start)  # Добавляем к списку новый первый элемент
    return lst


# Тесты
print(change([1, 2, 3]))
print(change([1, 2, 3, 4, 5]))
print(change(['н', 'л', 'о', 'с']))


#Второй способ занимает меньше кода, но не всегда очевиден.
#Решение - IDE

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Тесты
print(change([1, 2, 3]))
print(change([1, 2, 3, 4, 5]))
print(change(['н', 'л', 'о', 'с']))
