from timeit import timeit

result: float = timeit('"-".join(str(n) for n in range(100))', number=10000)
print(result)

first: float = timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(first)

second: float = timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(second)

third: float = timeit('"-".join(map(str, [n for n in range(100)]))', number=10000)
print(third)

fourth: float = timeit('map(lambda n: "-".join(str(n)), list(range(100)))', number=10000)
print(fourth)

print("-".join(str(list(range(100))).split(', ')))
fifth = [print(i, end='-') for i in list(range(100))]
print()
print(timeit(str(fifth), number=10000))
print("-".join([str(n) for n in range(100)]))
print("-".join([str(n) for n in range(100)]))
print("-".join(map(str, [n for n in range(100)])))

