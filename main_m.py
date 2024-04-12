# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pprint import pprint

from dmenu import DynamicMenu, COLOR_OFF, COLOR_YELLOW


class Project(DynamicMenu):
    # def print_option_1(self, menu_id=1):
    #     match menu_id:
    #         case 1:
    #             print(f"{COLOR_YELLOW}1:{COLOR_OFF} Create project.")
    #
    # def print_option_2(self, menu_id=1):
    #     match menu_id:
    #         case 1:
    #             print(f"{COLOR_YELLOW}2:{COLOR_OFF} View all project.")
    #
    # def print_option_3(self, menu_id=1):
    #     match menu_id:
    #         case 1:
    #             print(f"{COLOR_YELLOW}3:{COLOR_OFF} Edit project.")
    #
    # def print_option_4(self, menu_id=1):
    #     match menu_id:
    #         case 1:
    #             print(f"{COLOR_YELLOW}4:{COLOR_OFF} Delete project."
    def back_func(self, menu_id=1):
        pass

    def __init__(self, menu_items, back_func):
        super().__init__(menu_items, back_func)
        # default_menu = {
    #     1: option_1(),
    #     2: option_2(),
    #     3: option_3(),
    #     4: option_4(),
    #     5: option_5(),
    #     6: option_6(),
    #     7: option_7(),
    #     8: option_8(),
    #     9: option_9()
    # }
    # def __new__(cls, *args, **kwargs):
    #     # if not hasattr(cls, 'menu_items') or hasattr(cls, 'menu_items') and not cls.menu_items:
    #     #     cls.menu_items = {
    #     #         1: cls.print_option_1(self),
    #     #         2: cls.print_option_2(self),
    #     #         3: cls.print_option_3(self),
    #     #         4: cls.print_option_4(self),
    #     #         5: cls.print_option_5(self),
    #     #         6: cls.print_option_6(self),
    #     #         7: cls.print_option_7(self),
    #     #         8: cls.print_option_8(self),
    #     #         9: cls.print_option_9(self),
    #     #     }
    #     #     if not hasattr(cls, 'back_func') or hasattr(cls, 'back_func') and not cls.back_func:
    #     #         cls.back_func = cls.back_func
    #     #     if not hasattr(cls, '_instance'):
    #     #         cls._instance = super().__new__(cls, cls.menu_items, cls.back_func)
    #     #     return cls._instance


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def testing_my_menu():
    # default_menu = {
    #     1: print_option_1(self),
    #     2: print_option_2(self),
    #     3: print_option_3(self),
    #     4: print_option_4(self),
    #     5: print_option_5(self),
    #     6: print_option_6(self),
    #     7: print_option_7(self),
    #     8: print_option_8(self),
    #     9: print_option_9(self),
    # }
    menu_items = None
    back_func = None
    p1 = Project(menu_items, back_func)
    p1.loop_of_menu()
    # m1 = Menu(default_menu, do_next_option)
    # m1.loop_of_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Test menu')
    testing_my_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
