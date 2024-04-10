import filedb
import tasks
import projects


def main():
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


if __name__ == '__main__':
    print('Бібліотека керування проектами')
    main()
