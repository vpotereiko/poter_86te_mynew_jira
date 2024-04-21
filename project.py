from dmenu import DynamicMenu, COLOR, COLOR_YELLOW, COLOR_OFF
from filedb import FileDB


class Project(DynamicMenu, FileDB):
    _proj_items = []

    # _menu_items = []

    def __new__(cls, name=''):
        if name !='':
            create_project = super().__new__(cls)
            cls._proj_items.append(create_project)
            return create_project

    def __init__(self, proj_name):
        self.proj_name = proj_name
        self.file = FileDB(self)
        self.proj_id = self.file.proj_id

    def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd'):
        if menu_id == int(0) and menu_option == 'main_app_menu':
            m_items = {
                0: f'\tГоловне меню',
                1: f'{COLOR['blue']}Створити новий проект{COLOR_OFF}',
                2: f'{COLOR['blue']}Переглянути список проектів{COLOR['green']}({len(Project._proj_items)}){COLOR_OFF}',
                3: f'{COLOR['blue']}Редагувати проект{COLOR_OFF}',
                4: f'{COLOR['red']}Видалити проект !{COLOR_OFF}',
                5: f'{COLOR['green']}Відновити видалений проект{COLOR_OFF}',
            }
            # self.show_dmenu(m_items, 0) # для відладки промальовування
            self.loop_dmenu(self, (), m_items=m_items, item=0, first_item=1, last_item=6,
                            menu_id=0, menu_option='main_app_menu')
            return

    @staticmethod
    def show_selectable_items(self, *args, **kwargs):
        m_items = {
            0: f'\n{COLOR_YELLOW}Виберіть проект {COLOR['blue']}(лише перегляд):{COLOR_OFF}',
        }
        #
        # self.show_dmenu(m_items, 0)
        # print(self._proj_items)
        for i,val in enumerate(self._proj_items):
            # print(f'\t{i}. {self.menu_items[str(i-1)]}')
            m_upd = {
                (i+1):f'{COLOR['blue']}{val.proj_name}{COLOR_OFF}',
            }
            m_items.update(m_upd)
        self.loop_dmenu(self, (), m_items=m_items, item=0, first_item=len(self._proj_items) or 1,
                        last_item=len(self._proj_items)+1,
                        menu_id=1, menu_option='proj_list_readonly', list_items=self._proj_items)

    def show_item(self, *args, **kwargs):
        active_obj = self._proj_items[kwargs['selected_item']-1]
        m_items = {
            0: f'\n{COLOR_YELLOW}Проект {COLOR['blue']}{active_obj.proj_name}{COLOR_YELLOW}(лише перегляд):{COLOR_OFF}',
        }
        # #
        # # self.show_dmenu(m_items, 0)
        # # print(self._proj_items)
        index = 1
        for _,att in enumerate(dir(active_obj)):
            # print(att, getattr(your_object, att))
            if att[0:2] == '__' or att[0:1] == '_' or callable(getattr(active_obj, att)):
                continue
            m_upd = {
                index: f'{COLOR_YELLOW}<{att}> : {COLOR['blue']}{str(getattr(active_obj, att))}{COLOR_OFF}',
            }
            m_items.update(m_upd)
            index += 1

        self.loop_dmenu(self, (), m_items=m_items, item=0, first_item=1,
                        last_item=len(m_items),
                        menu_id=2, menu_option='proj_view_readonly', active_obj=active_obj)

    def get_method(self, *args, **kwargs):
        args = args or []
        kwargs = kwargs or {}
        if len(args) > 0:
            method_params = kwargs or {
                'menu_id': 0,
                'menu_option': 'main_app_menu'
            }
            if 'selected_item' in kwargs:
                selected_item = kwargs.get('selected_item', None)
                if selected_item is not None:
                    if kwargs['menu_id'] == 0 and kwargs['menu_option'] == 'main_app_menu':
                        match selected_item:
                            case 0:
                                self.menu_items[str(selected_item)]()
                            case 1:
                                self.menu_items[str(selected_item)]()
                            case 2:
                                self.show_selectable_items(*args, **kwargs)
                            case 3:
                                self.menu_items[str(selected_item)]()
                            case 4:
                                self.menu_items[str(selected_item)]()
                            case 5:
                                self.menu_items[str(selected_item)]()
                            case _:
                                print(f"Your choice out of range ({kwargs['first_item']}-{kwargs['last_item']}")
                                kwargs['selected_item'] = None
                                return self.loop_of_menu(*args, **kwargs)
                    elif kwargs['menu_id'] == 1 and kwargs['menu_option'] == 'proj_list_readonly':
                        for i,val in enumerate(self._proj_items):
                            if (i+1) == selected_item:
                                self.show_item(*args, **kwargs)
                    else:
                        print(f"Your choice out of range ({kwargs['first_item']}-{kwargs['last_item']}")
                        kwargs['selected_item'] = None
                        return self.loop_of_menu(*args, **kwargs)
                    #
                    # else:
                    #     if selected_item == self.last_item:
                    #         if callable(self.back_func):
                    #             self.back_func()
                    #             pass
                    #         else:
                    #             print(f"{COLOR['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                    #             self.menu_items[str(self.selected_item)]()
                    #             print(f"{COLOR['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                    #     else:
                    #         self.selected_item = selected_item
                    #         self.menu_items[str(self.selected_item)]()
            method_name = list(args).pop()
        else:
            pass
            method_name = 'dynamic_menu_method_d'  # (self, menu_id: int = 1, menu_option: str = 'd')
        # якщо не передали жодних параметрів
        method = getattr(self, method_name)
        return method(**method_params)  # method(self)