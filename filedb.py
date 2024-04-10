from tasks import Tasks as Task
from projects import Projects as Project,FILES_PATH


class ProjectFile(Project):
    """
    Завантаження та вивантаження проекту через json:
    <proj_id>_proj_<proj_slug_name>.json
    """
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


class TaskFile:
    """
    Завантаження та вивантаження завдання через json:
    <proj_id>_task_<task_slug_name>_<task_id>.json

    """
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
