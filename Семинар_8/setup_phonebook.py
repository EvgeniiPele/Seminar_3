def open_phonebook():
    with open('phonebook.txt', 'r') as data:
        print(data.read())
def save_phonebook():
    with open('phonebook.txt', 'r') as data:
        old_data = data.read()
    with open('phonebook.txt', 'w') as new:
        new.write(old_data)
    print('Файл сохранен')
def show_contact():
    with open('phonebook.txt', 'r') as data:
        print(data.read())

def add_contact():
    user_input = input('Введите контакт: ')
    with open('phonebook.txt', 'a+') as data:
        data.writelines("%s\n" % user_input)

def find_contact():
    user_find = input('Введите номер или имя: ').title()
    with open('phonebook.txt', 'r+') as data:
        for line in data:
            if user_find in line:
                print(line)



def edit_contact():
    user_find = input('Введите номер или имя, которое хотите изменить: ').title()
    new_contact = input('Введите новое имя, номер и комментарий: ')

    with open('phonebook.txt', 'r') as data:
        old_data = data.read()
    new_data = old_data.replace(user_find, new_contact, 1)
    with open('phonebook.txt', 'w') as new:
        new.write(new_data)


def delete_contact():
    number_delete = input('Введите номер или имя контакта, который хотите удалить: ')
    with open('phonebook.txt', 'r') as data:
        lines = data.readlines()
    with open('phonebook.txt', 'w') as new:
        for line in lines:
            if number_delete not in line:
                new.write(line)

