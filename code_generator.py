from datetime import datetime


class CodeGenerator:
    __counter = 0
    __items = []

    # @property
    # def valid_keys(self):
    #     keys = []
    #     for key in os.listdir(FILES_PATH):
    #         keys.append(key)
    #     return keys
    #
    # @staticmethod
    # def generate_new_key():
    #     dt = datetime.now()
    #     ts = datetime.timestamp(dt)
    #     return str(int(ts))  # string.digits
    #
    # @staticmethod
    # def get_date_fromtimestamp(ts_str):
    #     ts = int(ts_str)
    #     date_obj = datetime.fromtimestamp(ts)
    #     return date_obj
    def __new__(cls):
        cls.__counter += 1
        # dt = datetime.now()
        value = int(datetime.timestamp(datetime.now()) * 1_000_000)  # враховуєм мілісекунди при генерації ключа
        cls.__items.append(value)
        if len(cls.__items) != len(set(cls.__items)):
            pass
            # Якщо вже є ключі потрібно спробувати завантажи дані по раніше створених проектах і завданнях з файлів,
            # які створилися при:
            #   - виході з будь якого меню в програмі (створити, редагувати, видалити, вийти з програми).
            #   - після видалення об'єктів у програмі - файл не видаляється а переіменовується
            #   *<proj_id>*_ при видаленні проекту або _*<task_id>*_ при видаленні завдання
            #
            # Для цього шукаємо файли з ключами
            # Class attribute __items of code_generator. CodeGenerator
            #
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
            # raise ValueError('Ключі не можуть повторюватися!')
        return super().__new__(cls)

    def __init__(self):
        self.__id = self.__items[-1]

    def __str__(self):
        return str(self.__id)
