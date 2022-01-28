
try:
    with open('people.txt', 'r', encoding='utf-8') as people:
        out_error, count = 0, 0
        for row, line in enumerate(people, 1):
            count += len(line.strip())
            if len(line.strip()) < 3:
                out_error += 1
                error = open('errors.log', 'a', encoding='utf-8')
                error.write(f'Длина имени {line.strip()} менее 3-х символов. Ошибка в {row} строке\n')
                error.close()
        if out_error > 0:
            raise BaseException('В тексте есть имена с длиной символов менее 3-х. Смотрите лог')
finally:
    with open('errors.log', 'r', encoding='utf-8') as error:
        print(error.read())
    print('Кол-во символов в тексте:', count)
