
from pprint import pprint


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


def option_1(menu_id=1):
    print(f"P1 with {menu_id=}")
    print()


def option_2(menu_id=1):
    print(f"P2 with {menu_id=}")
    print()


def option_3(menu_id=1):
    print(f"P3 with {menu_id=}")
    print()


def option_4(menu_id=1):
    print(f"P4 with {menu_id=}")
    print()


def option_5(menu_id=1):
    print(f"P5 with {menu_id=}")
    print()


def option_6(menu_id=1):
    print(f"P6 with {menu_id=}")
    print()


def option_7(menu_id=1):
    print(f"P7 with {menu_id=}")
    print()


def option_8(menu_id=1):
    print(f"P8 with {menu_id=}")
    print()


def option_9(menu_id=1):
    print(f"P9 with {menu_id=}")
    print()


def do_next_option(menu_id=1):
    print(f"GO BACK SELECTED WITH {menu_id=}")

#
# menu_id9 = {
#     1: option_1,
#     2: option_2,
#     3: option_3,
#     4: option_4,
#     5: option_5,
#     6: option_6,
#     7: option_7,
#     8: option_8,
#     9: option_9
# }


# class Project(Menu):
#     def option_1(self, menu_id=1):
#         print(f"P1 with {menu_id=}")
#         print()
#
#     def option_2(self, menu_id=1):
#         print(f"P2 with {menu_id=}")
#         print()
#
#     def option_3(self, menu_id=1):
#         print(f"P3 with {menu_id=}")
#         print()
#
#     def option_4(self, menu_id=1):
#         print(f"P4 with {menu_id=}")
#         print()
#
#     def option_5(self, menu_id=1):
#         print(f"P5 with {menu_id=}")
#         print()
#
#     def option_6(self, menu_id=1):
#         print(f"P6 with {menu_id=}")
#         print()
#
#     def option_7(self, menu_id=1):
#         print(f"P7 with {menu_id=}")
#         print()
#
#     def option_8(self, menu_id=1):
#         print(f"P8 with {menu_id=}")
#         print()
#
#     def option_9(self, menu_id=1):
#         print(f"P9 with {menu_id=}")
#         print()
#
#     def back_func(self, menu_id=1):
#         do_next_option(menu_id)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(self)
#         pprint.PrettyPrinter(f"{self.__dict__=}")
#

class Menu:
    """
    A class that represents a menu
    """
    # def __new__(cls, *args, **kwargs):
    #     pprint(f"{cls=}")
    #     pprint(f"{args=}")
    #     pprint(f"{kwargs=}")
    #     return super().__new__(cls, *args, **kwargs)
    # def option_1(self, menu_id=1):
    #     pass # self.owner.option_1(menu_id)
    #
    # def option_2(self, menu_id=1):
    #     pass # self.owner.option_2(menu_id)
    #
    # def option_3(self, menu_id=1):
    #     pass # self.owner.option_3(menu_id)
    #
    # def option_4(self, menu_id=1):
    #     pass # self.owner.option_4(menu_id)
    #
    # def option_5(self, menu_id=1):
    #     pass # self.owner.option_5(menu_id)
    #
    # def option_6(self, menu_id=1):
    #     pass # self.owner.option_6(menu_id)
    #
    # def option_7(self, menu_id=1):
    #     pass # self.owner.option_7(menu_id)
    #
    # def option_8(self, menu_id=1):
    #     pass # self.owner.option_8(menu_id)
    #
    # def option_9(self, menu_id=1):
    #     pass # self.owner.option_9(menu_id)
    #
    # def back_func(self, menu_id=1):
    #     pass # self.owner.back_func(menu_id)

    def __new__(cls, menu_items, back_func):
        pprint(f"174{cls=}")
        pprint(f"175{menu_items=}")
        pprint(f"176{back_func=}")
        return super().__new__(cls)

    def __init__(self, menu_items, back_func):
        pprint(f"180{self=}")
        pprint(f"181{menu_items=}")
        pprint(f"182{back_func=}")
        # self.options = {
        #     1: self.option_1(),
        #     2: self.option_2(),
        #     3: self.option_3(),
        #     4: self.option_4(),
        #     5: self.option_5(),
        #     6: self.option_6(),
        #     7: self.option_7(),
        #     8: self.option_8(),
        #     9: self.option_9()
        # }
        # self.owner = None
        self.back_func = back_func
        self.menu_items = menu_items
        # # self.selected_item = 0
        self.last_item = int(len(self.menu_items)) + 1

    def show_menu(self, item=1,):
        if (item == 1):
            print(f"{yellow}{self.__class__} menu {off}")
        print(f"{yellow}{item}: {off} {self.menu_items[item].__name__}")

        if item == len(self.menu_items):
            print(f"{color_off}{self.last_item}{color_off} Exit")
            pass
        else:
            return self.show_menu(item + 1)

    def loop_of_menu(self):
        self.show_menu()
        try:
            print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
            self.selected_item = int(input("Enter your choice"))
            print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
            if self.selected_item < 1 or self.selected_item > self.last_item:
                print(f"Your choice out of range (1-{self.last_item}")
                return self.loop_of_menu()
            else:
                if self.selected_item == self.last_item:
                    if callable(self.back_func):
                        self.back_func()
                        pass
                    else:
                        print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                        self.menu_items[str(self.selected_item)]()
                        print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                        return self.loop_of_menu()
        except Exception as e:
            print(f"Error - try again:{str(e)}")
            return self.loop_of_menu()

    # @property
    # def options(self):
    #     # if self.options:
    #     #     return self.options
    #     # else:
    #     return {
    #         1: option_1,
    #         2: option_2,
    #         3: option_3,
    #         4: option_4,
    #         5: option_5,
    #         6: option_6,
    #         7: option_7,
    #         8: option_8,
    #         9: option_9
    #     }
    #
    # @options.setter
    # def set_options(self, value):
    #     match value:
    #         case 1:
    #             self.options = {
    #                 1: option_1
    #             }
    #         case 2:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2
    #             }
    #         case 3:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3
    #             }
    #         case 4:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4
    #             }
    #         case 5:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4,
    #                 5: option_5
    #             }
    #         case 6:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4,
    #                 5: option_5,
    #                 6: option_6
    #             }
    #         case 7:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4,
    #                 5: option_5,
    #                 6: option_6,
    #                 7: option_7
    #             }
    #         case 8:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4,
    #                 5: option_5,
    #                 6: option_6,
    #                 7: option_7,
    #                 8: option_8
    #             }
    #         case 9:
    #             self.options = {
    #                 1: option_1,
    #                 2: option_2,
    #                 3: option_3,
    #                 4: option_4,
    #                 5: option_5,
    #                 6: option_6,
    #                 7: option_7,
    #                 8: option_8,
    #                 9: option_9
    #             }
    #         case _:
    #             self.options = None
    #
    def __init__(self, menu_items, back_func):
        self.back_func = back_func
        self.menu_items = menu_items
        # self.selected_item = 0
        self.last_item = int(len(self.menu_items)) + 1

    def show_menu(self, item=1):
        if item == 1:
            print(f"{COLOR_YELLOW}{self.__class__} menu {COLOR_OFF}")
        print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} {self.menu_items[item].__name__}")

        if item == len(self.menu_items):
            print(f"{COLOR_YELLOW}{self.last_item}{COLOR_OFF} Exit")
            pass
        else:
            return self.show_menu(item + 1)

    def loop_of_menu(self):
        self.show_menu()
        try:
            print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
            self.selected_item = int(input("Enter your choice"))
            print(f"{color['darkblue']}{'-' * 5 * len(self.menu_items)}{off}")
            if self.selected_item < 1 or self.selected_item > self.last_item:
                print(f"Your choice out of range (1-{self.last_item}")
                return self.loop_of_menu()
            else:
                if self.selected_item == self.last_item:
                    if callable(self.back_func):
                        self.back_func()
                        pass
                    else:
                        print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                        self.menu_items[str(self.selected_item)]()
                        print(f"{color['darkgreen']}{'-' * 5 * len(self.menu_items)}{off}")
                        return self.loop_of_menu()
        except Exception as e:
            print(f"Error - try again:{str(e)}")
            return self.loop_of_menu()
