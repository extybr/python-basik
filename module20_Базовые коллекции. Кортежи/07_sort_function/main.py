# import random


def element_sort(number):
    for item in number:
        if type(item) is not int:
            return number
    return tuple(sorted(number))

# def element_sort(number):
#     for item in number:
#         if type(item) is not int:
#             return number
#     bubble = list(number)
#     for i in range(len(bubble)-1):
#         for j in range(len(bubble)-1-i):
#             if bubble[j] > bubble[j + 1]:
#                 bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
#     return tuple(bubble)


# numbers = tuple(random.randint(-50, 50) for i in range(10))

numbers = (6, 3, -1, 8, 4, 10, -5)
output = element_sort(numbers)
print(f'Ответ в консоли: {output}')

# зачет!

