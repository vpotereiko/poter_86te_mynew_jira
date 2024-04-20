from task import (Task)
from project import (Project)
from filedb import (FileDB)
from dmenu import (DynamicMenu)

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
