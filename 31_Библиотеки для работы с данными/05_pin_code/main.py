from itertools import permutations

pin_code = '0562'
combinations = permutations(range(10), 4)
for number in combinations:
    if '{}{}{}{}'.format(number[0], number[1], number[2], number[3]) == pin_code:
        print(number)
        break

# [print(number) for number in combinations if '{}{}{}{}'.format(number[0], number[1], number[2],
#                                                                number[3]) == pin_code]
