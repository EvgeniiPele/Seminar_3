import setup_phonebook

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
    p = setup_phonebook.Phonebook('phonebook.txt')
    match user_choice:
        case 1:
            p.open()
        case 2:
            p.save()
        case 3:
            p.show()
        case 4:
            p.add()
            print('Контакт добавлен')
        case 5:
            p.find()
        case 6:
            p.edit()
            print('Контакт изменен')
        case 7:
            p.delete()
            print('Контакт удален')
        case 8:
            break


setup_menu()