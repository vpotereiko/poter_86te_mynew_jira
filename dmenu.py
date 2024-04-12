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
    # def show_menu(self, item=1,):
    #     if item == 1:
    #         print(f"{COLOR_YELLOW}{self.__class__} menu {COLOR_OFF}")
    #     print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} {self.menu_items[item].__name__}")
    #
    #     if item == len(self.menu_items):
    #         print(f"{COLOR_YELLOW}{self.last_item}{COLOR_OFF} Exit")
    #         pass
    #     else:
    #         return self.show_menu(item + 1)
    #
    # def loop_of_menu(self):
    #     self.show_menu()
    #     try:
    #         print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
    #         self.selected_item = int(input("Enter your choice"))
    #         print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
    #         if self.selected_item < 1 or self.selected_item > self.last_item:
    #             print(f"Your choice out of range (1-{self.last_item}")
    #             return self.loop_of_menu()
    #         else:
    #             if self.selected_item == self.last_item:
    #                 if callable(self.back_func):
    #                     self.back_func()
    #                     pass
    #                 else:
    #                     print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
    #                     self.menu_items[str(self.selected_item)]()
    #                     print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
    #                     return self.loop_of_menu()
    #     except Exception as e:
    #         print(f"Error - try again:{str(e)}")
    #         return self.loop_of_menu()
    def get_method(self, *args, **kwargs):
        method_name = 'dynamic_menu_method_d'  # (self, menu_id: int = 1, menu_option: str = 'd')
        args = args or []
        # TODO подумати над параметрами dynamic_menu_method_<menu_option>
        kwargs = kwargs or {}
        # якщо не передали жодних параметрів
        method_params = kwargs or {
            'menu_id': 1,
            'menu_option': 'd'
        }
        if 'method_name' in args:
            pass  # method_name = ''
        if 'method_params' in kwargs:
            pass
        method = getattr(self, method_name)
        # if len(method_params) == 'self':
        #     return method()  # method(self)
        # else:
        #     pass  # TODO return method( )  # method(self)
        return method()  # method(self)
