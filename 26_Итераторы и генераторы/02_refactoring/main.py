from collections.abc import Iterable

first = [2, 5, 7, 10]
second = [3, 8, 4, 9]
to_find = 56

# can_continue = True
# for x in first:
#     for y in second:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break
#


def find_number(number_one: int, number_two: int) -> Iterable[int]:
    yield number_one * number_two


[print('Found!!!', one, two) for two in second for one in first
 for result in find_number(one, two) if result == to_find]
