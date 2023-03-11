def menu() -> int:
    print('''Главное меню: 
          1. Открыть файл
          2. Сохранить файл
          3. Показать контакты
          4. Добавить контакт
          5. Найти контакт
          6. Изменить контакт
          7. Удалить контакт
          8. Выход''')
    choice = int(input('Выберите пункт меню: '))
    return choice


def show_contact(phone_book: list):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<10} '
                  f'{contact.get("phone"):<10} '
                  f'{contact.get("comment"):<10}')
        print()
    else:
        print('\nТелефонная книга не открыта или пуста\n')


def new_contact() -> dict:
    print()
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def change(book: list) -> tuple:
    show_contact(book)
    choice = int(input('Выберите контакт, который хотите изменить: '))
    name = input('Введите новое имя или нажмите Enter, если хотите оставить его без изменений: ')
    phone = input('Введите новый телефон Enter, если хотите оставить его без изменений: ')
    comment = input('Введите новый комментарий Enter, если хотите оставить его без изменений: ')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}


def input_request(text: str) -> str:
    request = input(f'Введите {text}')
    return request


def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер элемента, который хотите удалить: ')) - 1


def goodbye():
    print('Книга закрыта')

def save():
    print('Изменения сохранены')