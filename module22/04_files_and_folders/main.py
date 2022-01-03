import os


def get_size(directory, count_file, count_folder, directory_size):
    # print(f'Директория: {directory}')
    for file in os.listdir(directory):
        file_path = os.path.abspath(os.path.join(directory, file))
        if os.path.isfile(file_path) or os.path.islink(file_path):
            # print(os.path.abspath(file_path))
            size = os.path.getsize(file_path)
            # print(f'Размер файла <{file}>', '{:.0e} Байт'.format(size))
            count_file += 1
            directory_size += size
        elif os.path.isdir(file_path):
            # print('   Папка:   ', file_path)
            count_folder += 1
            count_file, count_folder, directory_size = get_size(file_path, count_file,
                                                                count_folder, directory_size)
        # else:
        #     print('ERROR')
    return count_file, count_folder, directory_size


path = input('Пожалуйста, введите путь до директории: ')
# path = os.path.abspath(os.path.join('..', '..', 'Module22'))
file_count, folder_count, size_directory = get_size(path, 0, 0, 0)
path_size = size_directory / 1024
print(f'Размер каталога (в Кб): {path_size}')
print(f'Количество подкаталогов: {folder_count}')
print(f'Количество файлов: {file_count}')
