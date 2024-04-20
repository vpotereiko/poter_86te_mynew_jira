from dmenu import DynamicMenu
from filedb import FileDB


class Task(DynamicMenu, FileDB):
    _task_items = []
    # _menu_items = []

    def __new__(cls, name, owner):
        create_task = super().__new__(cls)
        cls._task_items.append(create_task)
        return create_task

    def __init__(self, task_name, proj_owner):
        self.task_name = task_name
        self.proj_owner = proj_owner
        self.file = FileDB(self)
        self.task_id = self.file.task_id


