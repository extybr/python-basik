
def validation(line):
    try:
        if line.split()[0].isalpha():
            if (line.split()[1].find('@') and line.split()[1].find('.')) != -1:
                try:
                    if 9 < int(line.split()[2]) < 100:
                        registrations_good = open('registrations_good.txt', 'a', encoding='utf-8')
                        registrations_good.write(line)
                        registrations_good.close()
                    else:
                        registrations_bad = open('registrations_bad.txt', 'a', encoding='utf-8')
                        registrations_bad.write(
                            f'{line.strip()}   |-->   Поле возраст НЕ является числом от 10 до 99\n')
                        registrations_bad.close()
                except ValueError:
                    print('Поле возраст содержит не только цифры')
            else:
                registrations_bad = open('registrations_bad.txt', 'a', encoding='utf-8')
                registrations_bad.write(
                    f'{line.strip()}   |-->   Поле емейл НЕ содержит @ и .(точку)\n')
                registrations_bad.close()
        else:
            registrations_bad = open('registrations_bad.txt', 'a', encoding='utf-8')
            registrations_bad.write(
                f'{line.strip()}   |-->   Поле имени содержит НЕ только буквы\n')
            registrations_bad.close()
    except IndexError:
        print('НЕ присутствуют все три поля')
        registrations_bad = open('registrations_bad.txt', 'a', encoding='utf-8')
        registrations_bad.write(f'{line.strip()}   |-->   НЕ присутствуют все три поля\n')
        registrations_bad.close()


with open('registrations.txt', 'r', encoding='utf-8') as registrations:
    for lines in registrations:
        validation(lines)
