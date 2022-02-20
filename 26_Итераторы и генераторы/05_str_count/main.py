import os
from collections.abc import Iterable


def gen_files_path() -> Iterable[str]:
    for path, _, file in os.walk('..'):
        for files in file:
            if files.endswith('.py'):
                with open(os.path.join(path, files), 'r', encoding='utf-8') as script:
                    for line in script:
                        if len(line.strip().encode('utf-8')) != 0 and not line.strip().startswith(
                                '#'):
                            # print(line.strip())
                            yield 1


row = 0
for _ in gen_files_path():
    row += 1
print('Число строк в питоновских файлах', row)
