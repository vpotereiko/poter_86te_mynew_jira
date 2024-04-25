import pprint

COLOR = {
    'white': "\033[1;37m",
    'yellow': "\033[1;33m",
    'green': "\033[1;32m",
    'blue': "\033[1;34m",
    'cyan': "\033[1;36m",
    'red': "\033[1;31m",
    'magenta': "\033[1;35m",
    'black': "\033[1;30m",
    'darkwhite': "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen': "\033[0;32m",
    'darkblue': "\033[0;34m",
    'darkcyan': "\033[0;36m",
    'darkred': "\033[0;31m",
    'darkmagenta': "\033[0;35m",
    'darkblack': "\033[0;30m",
    'off': "\033[0;0m"
}
COLOR_YELLOW = "\033[1;33m"
COLOR_OFF = "\033[0;0m"


class DynamicMenu:
    """
    Клас для реалізації динамічного меню для будь яких класів, що наслідують цей клас.(<DynamicMenu>)
    Зручно перезавантажувати методи цього (Базового) класу у дочірніх класах що нослідують клас <DynamicMenu>, або
    виклику методу базового класу з екземпляром (self) ДОЧІРНЬОГО класу (напр.Project
    Наприклад.
    Метод по замовчуванню "def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd', *args, **kwargs):",
    який вкликається якщо жодних методів і додаткових параметрів не вказано або вказано невірно.

    Спрощений спосіб реалізації без додаткових параметрів та наслідування за посиланням нижче:
    https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
    class DynamicMenu():
        def method1(self):
            pass
        def method2(self):
            pass
        def method3(self):
            pass
        def get_method(self, method_name):
            method = getattr(self, method_name)
            return method()

    callbyname = DynamicMenu()
    method1 = callbyname.get_method(method_name)

    """

    def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd'):
        pass

    def dynamic_menu_method_1(self, menu_id: int = 1, menu_option: str = '1'):
        pass

    def dynamic_menu_method_2(self, menu_id: int = 1, menu_option: str = '2'):
        pass

    def dynamic_menu_method_3(self, menu_id: int = 1, menu_option: str = '3'):
        pass

    def dynamic_menu_method_4(self, menu_id: int = 1, menu_option: str = '4'):
        pass

    def dynamic_menu_method_5(self, menu_id: int = 1, menu_option: str = '5'):
        pass

    def dynamic_menu_method_6(self, menu_id: int = 1, menu_option: str = '6'):
        pass

    def dynamic_menu_method_7(self, menu_id: int = 1, menu_option: str = '7'):
        pass

    def dynamic_menu_method_8(self, menu_id: int = 1, menu_option: str = '8'):
        pass

    def dynamic_menu_method_9(self, menu_id: int = 1, menu_option: str = '9'):
        pass

    def dynamic_menu_method_10(self, menu_id: int = 1, menu_option: str = '10'):
        pass

    # def __init__(self, menu_items, back_func):
    #     self.back_func = back_func
    #     self.menu_items = menu_items
    #     self.selected_item = 0
    #     self.last_item = int(len(self.menu_items)) + 1
    #
    def show_dmenu(self, *args, **kwargs):
        item = kwargs.get('item', 0)
        menu_items = kwargs.get('m_items', {})
        first_item = kwargs.get('first_item', item)
        last_item = kwargs.get('last_item', len(menu_items))
        if 0 <= item <= last_item:
            if item == last_item:
                print(f"{COLOR_YELLOW}{last_item}: {COLOR['red']} Вихід{COLOR_OFF}")
            else:
                if item >= first_item:
                    if isinstance(menu_items[item], list):
                        print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} {menu_items[item][0]}", end='')
                        print(f"{menu_items[item][1]}", end='')
                        print(f"{menu_items[item][2]}", end='\n')
                        # for i in range(1, len(menu_items[item]) - 1):
                        #     print(f"{menu_items[item][i]}")
                    else:
                        print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} {menu_items[item]}")
                else:
                    print(f"{menu_items[item]}")
        else:
            if item >= last_item:
                return
        item = kwargs.get('item', first_item) + 1
        kwargs['item'] = item
        return self.show_dmenu(*args, **kwargs)

    def loop_dmenu(self, *args, **kwargs):
        item = kwargs.get('item', 0)
        menu_items = kwargs.get('m_items', {})
        first_item = kwargs.get('first_item', item)
        last_item = kwargs.get('last_item', len(menu_items))
        selected_item = kwargs.get('selected_item', None)
        list_items = kwargs.get('list_items', None)
        self.show_dmenu(*args, **kwargs)
        try:
            print(f"{COLOR['darkblue']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
            selected_item = int(input("Enter your choice"))
            print(f"{COLOR['darkblue']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
            if first_item > selected_item > last_item:
                print(f"Your choice out of range ({item}-{last_item}")
                return self.loop_dmenu(*args, **kwargs)
            else:
                # last_selected_item = kwargs.get('last_selected_item',selected_item)
                if selected_item and selected_item == last_item:
                    pass
                    # if callable(self.back_func):
                    #     self.back_func()
                    #     pass
                else:
                    print(f"{COLOR['darkgreen']}{'-' * 5 * last_item}{COLOR_OFF}")
                    kwargs['selected_item'] = selected_item
                    self.get_method(*args, **kwargs)
                    # menu_items[str(selected_item)]()
                    print(f"{COLOR['darkgreen']}{'-' * 5 * last_item}{COLOR_OFF}")
                    return self.loop_dmenu(*args, **kwargs)
        except Exception as e:
            print(f"Error - try again:{str(e)}")
            return self.loop_dmenu(*args, **kwargs)

    def get_method(self, *args, **kwargs):
        method_name = 'dynamic_menu_method_d'  # (self, menu_id: int = 1, menu_option: str = 'd')
        args = args or []
        if len(args) > 0:
            method_name = list(args).pop()
        kwargs = kwargs or {}
        # якщо не передали жодних параметрів
        method_params = kwargs or {
            'menu_id': 0,
            'menu_option': 'main_app_menu'
        }
        method = getattr(self, method_name)
        return method(**method_params)  # method(self)
