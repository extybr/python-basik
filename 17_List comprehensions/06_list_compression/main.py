
import random

numbers = int(input('Кол-во чисел: '))
compression = [random.randint(-3, 3) for _ in range(numbers)]
print(compression)
compression_not_zero = [index for index in compression if index]
compression_zero = [index for index in compression if not index]
compression_not_zero.extend(compression_zero)
print(compression_not_zero)
compression = [index for index in compression if index]
print(compression)

# зачет!

