# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pprint

from menu import Menu


# перевизначення дій в меню
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


menu_id9 = {
    1: option_1,
    2: option_2,
    3: option_3,
    4: option_4,
    5: option_5,
    6: option_6,
    7: option_7,
    8: option_8,
    9: option_9
}


class Project(Menu):
    # перевизначення дій в меню
    def option_1(self, menu_id=1):
        print(f"P1 with {menu_id=}")
        print()

    def option_2(self, menu_id=1):
        print(f"P2 with {menu_id=}")
        print()

    def option_3(self, menu_id=1):
        print(f"P3 with {menu_id=}")
        print()

    def option_4(self, menu_id=1):
        print(f"P4 with {menu_id=}")
        print()

    def option_5(self, menu_id=1):
        print(f"P5 with {menu_id=}")
        print()

    def option_6(self, menu_id=1):
        print(f"P6 with {menu_id=}")
        print()

    def option_7(self, menu_id=1):
        print(f"P7 with {menu_id=}")
        print()

    def option_8(self, menu_id=1):
        print(f"P8 with {menu_id=}")
        print()

    def option_9(self, menu_id=1):
        print(f"P9 with {menu_id=}")
        print()

    def back_func(self, menu_id=1):
        do_next_option(menu_id)

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        pprint.PrettyPrinter(f"{self.__dict__=}")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def testing_my_menu():
    m1 = Menu(menu_id9, do_next_option)
    m1.loop_of_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Test menu')
    testing_my_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
