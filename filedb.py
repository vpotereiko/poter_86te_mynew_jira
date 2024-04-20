import json
import os
from code_generator import CodeGenerator

FILES_PATHS = [
    os.path.dirname(os.path.dirname(__file__)),
]


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

    def __init__(self, instance):
        self.paths = FILES_PATHS
        if instance is not None:
            from task import Task
            if isinstance(instance, Task):
                self.task_id = str(CodeGenerator())
                self.proj_id = instance.proj_owner.file.proj_id
                self.proj_owner = instance.proj_owner
                self.file_name = f"{self.proj_id}_{self.task_id}_{instance.task_name}_at_{instance.proj_owner.proj_name}.json"
            else:  # project
                self.proj_id = str(CodeGenerator())
                self.proj_name = instance.proj_name
                self.file_name = f"{self.proj_id}_{self.proj_name}.json"

    def __str__(self):
        return f"{self.file_name}"

        # try:
        #     # взяти з _owner якщо заповнено
        #     if self._owner and instance(self,ProjectItem):
        #         self.proj_id = str(CodeGenerator())
        #     self.file_name = f"{self.proj_id}_{self._owner.name}.json"
        # except Exception as e:
        #     print(e)
        #     self.proj_id = str(CodeGenerator())
        #     self.task_id = str(CodeGenerator())
        #     self.file_name = f"{self.proj_id}_{self.task_id}_{self._owner.name}.json"

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
