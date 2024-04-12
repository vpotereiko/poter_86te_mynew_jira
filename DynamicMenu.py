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





