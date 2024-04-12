
from datetime import datetime
from dmenu import DynamicMenu




def edit_project_menu(key=1):
    print(f'Edit project_{key} menu')
    print('1. Edit project name')
    print('2. Edit project slug name')
    print('3. Edit project description')
    print('4. Edit project start date')
    print('5. Edit project end date')
    print('6. Edit project status')
    print('7. show project tasks')


def create_project():
    pass


def show_projects():
    pass


def edit_project(key=1):
    return edit_project_menu(key)




class Project:
    # _id = PrivateKey()

    def __init__(self, proj_name, proj_slug_name):
        self.proj_id = PrivateKey()
        self._proj_name = proj_name
        self._proj_slug_name = proj_slug_name

    @property
    def proj_slug_name(self):
        return self._proj_slug_name
