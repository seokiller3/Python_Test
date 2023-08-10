import os


def batch_rename_files(target_dir, new_name, num_digits, source_extension, target_extension, name_range=None):
    """Групповое переименование файлов в заданной директории."""
    if not os.path.exists(target_dir):
        print("Указанная директория не существует.")
        return

    files = [file for file in os.listdir(target_dir) if file.endswith(source_extension)]
    files.sort()

    counter = 1
    for file in files:
        base_name = file[:-len(source_extension)]  # Убираем исходное расширение

        if name_range:
            start, end = name_range
            new_base_name = base_name[start - 1:end] + new_name
        else:
            new_base_name = new_name

        new_file_name = f"{new_base_name}_{str(counter).zfill(num_digits)}.{target_extension}"
        source_path = os.path.join(target_dir, file)
        target_path = os.path.join(target_dir, new_file_name)

        os.rename(source_path, target_path)
        counter += 1


# Параметры
target_directory = "путь_к_папке"
new_name = "new_file"
num_digits = 3
source_extension = ".txt"
target_extension = "txt"
name_range = (3, 6)  # Диапазон символов для нового имени (если нужно)

# Вызываем функцию группового переименования
batch_rename_files(target_directory, new_name, num_digits, source_extension, target_extension, name_range)
