from dmenu import DynamicMenu
from filedb import FileDB


class Task(DynamicMenu, FileDB):
    _task_items = []
    # _menu_items = []

    def __new__(cls, name, desc, owner):
        create_task = super().__new__(cls)
        cls._task_items.append(create_task)
        owner.task_items.append(create_task)
        return create_task

    def __init__(self, task_name, task_desc, proj_owner):
        self.name = task_name
        self.desc = task_desc
        self.owner = proj_owner
        self.file = FileDB(self)
        self._id = self.file.task_id

    # menu_id = 3, menu_option = 4
    def create_new_task(self, *args, **kwargs):
        _input_items = {
            'new_task_name': '',
            'new_task_desc': '',
        }
        # Task('task1', p1)
        new_task_obj = Task(_input_items['new_task_name'], _input_items['new_task_desc'],)
        print(f"{COLOR['blue']}({new_proj_obj.name}){COLOR_YELLOW}Створення нового завдання:{COLOR_OFF}")
        print(f"{COLOR_YELLOW} 1: Назва завдання:{COLOR['blue']}")
        _input_items["new_task_name"] = input('>')
        print(f"{COLOR_YELLOW} 2: Опис завдання:{COLOR['blue']}")
        _input_items['new_task_desc'] = input('>')
        #
        m_items = {
            0: f"{COLOR['blue']}({new_proj_obj.name}){COLOR_YELLOW}Створення завдання проекту:{COLOR_OFF}",
            1: [
                f"{COLOR_YELLOW}Назва завдання:{COLOR['blue']}",
                _input_items["new_task_name"],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],
            # 2: f"{COLOR_YELLOW}Опис проекту:{COLOR['blue']}{kwargs.get('new_proj_desc', '')}{COLOR['green']}(
            # змінити){COLOR_OFF}",
            2: [
                f"{COLOR_YELLOW}Опис завдання:{COLOR['blue']}",
                _input_items['new_task_desc'],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],

            3: f"{COLOR_YELLOW}Переглянути всі завдання {COLOR['green']}({len(new_proj_obj.task_items)}){COLOR_OFF}",
            4: f"{COLOR['green']}Зберегти {COLOR['blue']} і додати нове завдання{COLOR_OFF}",
            5: f"{COLOR['green']}Зберегти завдання та проект {COLOR_OFF}",
        }
        # input_items = kwargs.get('input_items', _input_items)
        # selected_item = kwargs.get('selected_item', None)
        # list_items = kwargs.get('list_items', None)
        # first_item = kwargs.get('first_item', 1)
        # last_item = kwargs.get('last_item', 6)
        self.loop_dmenu(new_proj_obj, m_items=m_items, item=0, first_item=1, last_item=6,
                        menu_id=4, menu_option='task_new_create',
                        new_task_name=_input_items["new_task_name"],
                        new_task_desc=_input_items['new_task_desc'],
                        input_items=_input_items,
                        new_proj_obj=new_proj_obj,
                        task_items=new_task_obj.task_items)



