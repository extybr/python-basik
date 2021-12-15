""" Задача 2. Кризис фруктов

Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре в виде пар «название фрукта — доход»: 

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
} 

В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.

Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря. Выведите итоговый словарь на экран.

Результат работы программы:
Общий доход за год составил 35419.34 рублей
Самый маленький доход у grapefruit. Он составляет 300.4 рублей
Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0} """

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
profit = sum(incomes.values())
minimum = min(incomes.values())
# print(len(incomes))
for product in list(incomes.items()):
    if product[1] == minimum:
        delete_product = product[0]
        incomes.pop(product[0])
# print(len(incomes))
print('Общий доход за год составил {0} рублей'.format(profit))
print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(delete_product, minimum))
print('Итоговый словарь: {0}'.format(incomes))