from setup_phonebook import open_phonebook
from setup_phonebook import show_contact
from setup_phonebook import add_contact
from setup_phonebook import find_contact
from setup_phonebook import edit_contact
from setup_phonebook import delete_contact
from setup_phonebook import save_phonebook


def setup_menu():
    print('Меню:\n'
        '1. Открыть файл\n'
        '2. Сохранить файл\n'
        '3. Показать контакты\n'
        '4. Добавить контакты\n'
        '5. Найти контакт\n'
        '6. Изменить контакт\n'
        '7. Удалить контакт\n'
        '8. Выход')
    data = int(input('Выберите нужню цифру: '))
    return data

while True:
    user_choice = setup_menu()
    match user_choice:
        case 1:
            open_phonebook()
        case 2:
            save_phonebook()
        case 3:
            show_contact()
        case 4:
            add_contact()
            print('Контакт добавлен')
        case 5:
            find_contact()
        case 6:
            edit_contact()
            print('Контакт изменен')
        case 7:
            delete_contact()
            print('Контакт удален')
        case 8:
            break


setup_menu()