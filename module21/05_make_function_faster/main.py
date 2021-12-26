
def calculating_math_function(data, cache={}):
    cache = cache if isinstance(cache, dict) else dict()
    if data in cache:
        return cache[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    cache[data] = result
    return cache[data]


my_numbers = list(range(1, 10))
full = dict()
for number in my_numbers:
    calculating_math_function(number, full)
print(full)

my_number = int(input('Введите число: '))
output = calculating_math_function(my_number, full)
print(output)
