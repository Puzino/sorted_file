import os

# путь к папке
folder_path = 'c:\\Users\\User\\Downloads\\'
# folder_path = 'd:\\downloads'
# Ключи - названия папок для каждой отдельной папки
extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv',
              'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'font': ['otf', 'ttf', 'fon', 'fnt'],

    'gif': ['gif'],

    'bat': ['bat'],

    'apk': ['apk'],

    'exe': ['exe'],

    'folder-name': ['extension-name', 'another-extension']
}

# Функция для создания папок
def create_folder_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')




# Передаём функцию для получения путей подпапок для каждого объекта
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


# Берет пути папок
def get_subfolder_names(folders_path) -> list:
    subfolder_paths = get_subfolder_paths(folders_path)
    subfolder_names = [f.split('\\')[-1] for f in subfolder_paths]

    return subfolder_names


# Получает пути всех папок
def get_file_paths(folder_path):
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


# получает имена файлов

def get_file_names(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    file_names = [f.split('\\')[-1] for f in file_paths]

    return file_names


# сортирует файлы
def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    # цикл для каждого пути файла в списке. Вытащим отдельно расширение и имя файла.

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                # os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_path = get_subfolder_paths(folder_path)

    for p in subfolder_path:
        if not os.listdir(p):
            print('Deleting empty folder', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    # print("# # # Creating folders # # #\n")
    create_folder_from_list(extensions)

    print("# # # Sorting files # # #\n")
    sort_files(folder_path)

    print("# # # Removing empty folders # # #\n")
    remove_empty_folders(folder_path)