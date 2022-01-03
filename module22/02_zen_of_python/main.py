
zen = open('zen.txt', 'r')
lines = zen.readlines()
[print(line.strip()) for line in reversed(lines)]
zen.close()

# zen = open('zen.txt', 'r')
# lines = zen.readlines()
# for line in reversed(lines):
#     print(line.strip())
# zen.close()
