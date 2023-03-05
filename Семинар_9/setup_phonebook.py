

class Phonebook:

    def __init__(self, phonebook):
        self.phonebook = phonebook

    def open(self):
        with open(self.phonebook, 'r') as data:
            print(data.read())

    def save(self):
        with open(self.phonebook, 'r') as data:
            old_data = data.read()
        with open('self.phonebook', 'w') as new:
            new.write(old_data)
        print('Файл сохранен')
    def show(self):
        with open(self.phonebook, 'r') as data:
            print(data.read())

    def add(self):
        user_input = input('Введите контакт: ')
        with open(self.phonebook, 'a+') as data:
            data.writelines("%s\n" % user_input)

    def find(self):
        user_find = input('Введите номер или имя: ').title()
        with open(self.phonebook, 'r+') as data:
            for line in data:
                if user_find in line:
                    print(line)



    def edit(self):
        user_find = input('Введите номер или имя, которое хотите изменить: ').title()
        new_contact = input('Введите новое имя, номер и комментарий: ')

        with open(self.phonebook, 'r') as data:
            old_data = data.read()
        new_data = old_data.replace(user_find, new_contact, 1)
        with open(self.phonebook, 'w') as new:
            new.write(new_data)


    def delete(self):
        number_delete = input('Введите номер или имя контакта, который хотите удалить: ')
        with open(self.phonebook, 'r') as data:
            lines = data.readlines()
        with open(self.phonebook, 'w') as new:
            for line in lines:
                if number_delete not in line:
                    new.write(line)

