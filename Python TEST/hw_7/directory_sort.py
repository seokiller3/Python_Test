"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os
import shutil


def sort_files_by_extension(source_folder, target_folder, file_categories):
    """Сортирует файлы по директориям на основе заданных расширений."""
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_extension = file.split('.')[-1].lower()
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    category_folder = os.path.join(target_folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(category_folder, file)
                    shutil.move(source_path, target_path)
                    break


# Исходная папка, куда помещены файлы
source_folder = "исходная_папка"

# Папка, в которой будут созданы директории для сортировки
target_folder = "папка_с_сортировкой"

# Словарь, где ключи - это названия категорий, а значения - списки расширений файлов для каждой категории
file_categories = {
    "видео": ["mp4", "avi", "mkv"],
    "изображения": ["jpg", "png", "gif"],
    "текст": ["txt", "docx", "pdf"],
    # Добавьте другие категории и соответствующие расширения здесь
}

# Вызываем функцию сортировки
sort_files_by_extension(source_folder, target_folder, file_categories)
