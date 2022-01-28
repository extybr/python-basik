import os


def find_file(project_path, file_name):
    print('\nСодержимое папки: ')
    for i in os.listdir(project_path):
        path = os.path.abspath(os.path.join(' ', project_path, i))
        print('Смотрим ', path)
        if i == file_name:
            if os.path.isfile(path):
                return print('Это файл'), path
            elif os.path.islink(path):
                return print('Это ссылка'), path
            elif os.path.isdir(path):
                return print('Это папка'), path
        if os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..', 'PycharmProjects')), 'main.py')

if file_path:
    print('Абсолютный путь:', file_path)
else:
    print('Файл не найден')