import os


def find_file(project_path, file_name):
    for i in os.listdir(project_path):
        path = os.path.abspath(os.path.join(' ', project_path, i))
        if i == file_name:
            if os.path.isfile(path):
                print(f'Путь к файлу <{file_name}>: {path}')
            elif os.path.islink(path):
                print(f'Путь к ссылке {file_name}: {path}')
            elif os.path.isdir(path):
                print(f'Путь к папке <{file_name}>: {path}')
        elif os.path.isdir(path):
            find_file(path, file_name)


find_file(os.path.abspath(
    os.path.join('..', '..', 'PycharmProjects')), '.gitignore')