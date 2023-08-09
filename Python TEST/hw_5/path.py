import os


def split_file_path(file_path):
    # Разделяем абсолютный путь на путь к директории и имя файла
    directory, file_name = os.path.split(file_path)

    # Разделяем имя файла на имя и расширение
    file_name, file_extension = os.path.splitext(file_name)

    return directory, file_name, file_extension


absolute_path = "/home/user/documents/example.txt"
directory, file_name, file_extension = split_file_path(absolute_path)
print("Путь:", directory)
print("Имя файла:", file_name)
print("Расширение файла:", file_extension)
