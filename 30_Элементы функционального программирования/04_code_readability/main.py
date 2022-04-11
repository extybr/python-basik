result = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))),
                     range(2, 1000)))
print('Нахождение простых чисел через лямбда функцию\n', result)

sieve = list(range(1000))
sieve[1] = 0
for number in range(2, 1000):
    if sieve[number] != 0:
        elem = number * 2
        while elem < 1000:
            sieve[elem] = 0
            elem += number
result_1 = [number for number in sieve if number != 0]
print('Нахождение простых чисел через решето Эратосфена\n', result_1)

new = list()
sieve_1 = set(range(2, 1000))
while sieve_1:
    prime = min(sieve_1)
    new.append(prime)
    sieve_1 -= set(range(prime, 1000, prime))
print('Аналог решета Эратосфена\n', new)


def is_prime(item):
    divider = 2
    while item % divider != 0 and divider <= item - 1:
        divider += 1
    if item == divider:
        return item


result_2 = [i for i in list(range(2, 1000)) if is_prime(i)]
print('Нахождение простых чисел через функцию\n', result_2)
