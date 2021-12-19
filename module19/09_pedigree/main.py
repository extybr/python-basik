
number = int(input('Введите количество человек: '))
pedigree, parent = dict(), dict()

for peoples in range(1, number):
    man, woman = input(f'{peoples} пара: ').split()
    parent[man] = woman
    pedigree[man] = 0
    pedigree[woman] = 0

for people in parent:
    temp = people
    while temp in parent:
        temp = parent[temp]
        pedigree[people] += 1

print('\n“Высота” каждого члена семьи:')
for people in sorted(pedigree):
    print(people, pedigree[people])
# print(pedigree, parent)
