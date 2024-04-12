from dmenu import DynamicMenu
from task import Task
from project import Project, PrivateKey, FILES_PATH


def main():


    class DynamicMenu():
        def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd'):
            # меню
            print('Головне меню')
            print('1. Створити проект')
            print('2. Переглянути список проектів')
            print('3. Редагувати проект')
            user_choice = int(input("(1-3)?"))
            if user_choice == 1:
                projects.create_project()
            elif user_choice == 2:
                projects.show_projects()
            elif user_choice == 3:
                projects.edit_project(
                    input('Введіть номер проекта в списку або ідентифікатор: '))

        def get_method(self, method_name):
            method = getattr(self, method_name)
            return method()

    main_proj = Project()
    dynamic_menu_method_d = callbyname.get_method('dynamic_menu_method_d')


if __name__ == '__main__':
    print('Бібліотека керування проектами')
    main()
