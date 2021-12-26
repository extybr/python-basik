
def calculate_sum(first, second):
    for item in first:
        if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, dict):
            calculate_sum(item, second)
        if isinstance(item, int) or isinstance(item, float):
            second.append(item)
        if type(first) is dict:
            if type(first[item]) is int:
                second.append(first[item])
    summa = 0
    for element in second:
        summa += element
    return summa


old = [[1, 2, [3]], [1], 3]
# old = [[3], [1], 6]
# old = {'J': 1, 'W': 3, 'A': 5, 'M': 7}
# old = {9: 'J', 4: 'J', 'F': 1, 8: 'M'}
# old = (1, 2, 3, 2, 3)
new = []
result = calculate_sum(old, new)
print(result)
