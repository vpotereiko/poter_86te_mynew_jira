import os
from string import digits
from datetime import datetime

FILES_PATH = os.path.join(os.path.dirname(__file__))


class PrivateKey:
    _id = str

    @property
    def valid_keys(self):
        keys = []
        for key in os.listdir(self.path):
            keys.append(key)
        return keys

    @staticmethod
    def generate_new_key():
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        return str(int(ts)) # string.digits

    def __init__(self):
        self._id = PrivateKey.generate_new_key()


class FileDB:
    """
    Базовий клас для завантаження та вивантаження дочірніх класів  через json-файли:
        <_id>_proj_<proj_slug_name>.json (формат імені файлу класу Project):
            <_id> - string.digits - timestamp - project id;
            <proj-slug-name> - string - project slug name службове ім'я проекту;
        <_id(1)>_task_<task_slug_name>_<_id(2)>.json (формат імені файлу класу Task)
            <_id(1)> - string.digits - timestamp - project id;
            <_id(2)> - string.digits - timestamp - task id;
            <task-slug-name> - string - project slug name службове ім'я завдання;
    """
    _id = PrivateKey.generate_new_key()
    path = FILES_PATH
    # def load_all_data(emp_path='def.json'):
    #     try:
    #         with open(emp_path, "r+") as f:
    #             empl, users = json.load(f)
    #     except Exception as e:
    #         print(e)
    #         return [{'e1': {'e_name': 'Vasia',
    #                         'e_surname': 'V3',
    #                         'e_birthday': '27-07-1978'
    #                         },
    #                  },
    #                 {'u1': 'p1'}
    #                 ]
    #     return empl, users
    #
    # def save_all_data(empl, users, f_path='def.json'):
    #     try:
    #         with open(f_path, "w") as f:
    #             json.dump([empl, users], f, indent=4)
    #             # json.dump(users, f, indent=4)
    #     except Exception as e:
    #         print(e)
