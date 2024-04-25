from task import (Task)
from project import (Project)
from filedb import (FileDB)
from dmenu import (DynamicMenu)

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


import pprint


def main():
    # main_proj = Project('Бібліотека керування проектами','p_lsb',)
    # main_proj.get_method('dynamic_menu_method_d')
    p1 = Project("Бібліотека керування проектами")
    print()
    pprint.pprint(f"{p1.__dict__=}")
    print()
    t1 = Task('task1', p1)
    pprint.pprint(f"{t1.__dict__=}")
    p1.get_method('dynamic_menu_method_d')


if __name__ == '__main__':
    print('Бібліотека керування проектами')
    main()
