import os
import json
import csv
import pickle


def calculate_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def traverse_and_save(directory):
    data = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            file_info = {
                'file_path': relative_path,
                'parent_directory': root,
                'size_bytes': os.path.getsize(file_path),
                'last_modified': os.path.getmtime(file_path),
                'type': 'file'
            }
            data.append(file_info)

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            relative_path = os.path.relpath(dir_path, directory)
            dir_info = {
                'file_path': relative_path,
                'parent_directory': root,
                'size_bytes': calculate_directory_size(dir_path),
                'type': 'directory'
            }
            data.append(dir_info)

    json_filename = 'result.json'
    csv_filename = 'result.csv'
    pickle_filename = 'result.pickle'

    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file,
                                    fieldnames=['file_path', 'parent_directory', 'size_bytes', 'last_modified', 'type'])
        csv_writer.writeheader()
        csv_writer.writerows(data)

    with open(pickle_filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == "__main__":
    directory_to_traverse = "your_dir"
    traverse_and_save(directory_to_traverse)
