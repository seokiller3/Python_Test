"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def convert_txt_to_json(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f, \
            open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)


convert_txt_to_json('task7_3.txt', 'task8_1.json')
