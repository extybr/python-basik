print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

summa = 0
factorial = 1
number = int(input('Введите число: '))
for _ in range(1, number + 1):
    for cycle in range(2, number + 1):
        factorial *= cycle
        #print(factorial)
        summa += factorial
        number -= number
print('Сумма факториалов:', summa + 1)
