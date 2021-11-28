
nice = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

numbers = [three for one in nice for two in one for three in two]
print(numbers)

# numbers = []
# for one in nice:
#     for two in one:
#         for three in two:
#             numbers.append(three)
# print(numbers)

# зачет!

