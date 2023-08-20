import json


class UserJSONHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_data(self):
        with open(self.filename, "w", encoding='utf-8') as js_f:
            json.dump(self.data, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)

    def add_user(self, name, user_id, level):
        user = {
            "name": name,
            "id": user_id,
            "level": level,
        }
        self.data.append(user)
        self._save_data()

    def run(self):
        s = 'n'
        while s != 'y':
            name = input("Введите имя: ")
            user_id = input("Введите id: ")
            level = int(input('Введите уровень доступа (1-7): '))
            self.add_user(name, user_id, level)
            s = input('Выход y/n: ')


if __name__ == "__main__":
    handler = UserJSONHandler('task8_2.json')
    handler.run()
