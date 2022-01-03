
numbers = open('numbers.txt', 'r')
item = numbers.readline()
number = int(item)
summa = sum([number for item in numbers])
numbers.close()

answer = open('answer.txt', 'w')
answer.write(str(summa))
answer.close()

numbers = open('numbers.txt', 'r')
content = numbers.read()
print(f'Содержимое файла numbers.txt\n', content)

# numbers = open('numbers.txt', 'r')
# print(f'Содержимое файла numbers.txt')
# [print(i, end='') for i in numbers]
numbers.close()

answer = open('answer.txt', 'r')
[print(f'\nСодержимое файла answer.txt\n{i}') for i in answer]
answer.close()
