class PhoneBook:

    def __init__(self, path: str = 'phone_book.txt'):
        self.path = path
        self.phone_book = []

    def open_file(self):
        with open(self.path, 'r') as file:
            data = file.readlines()
        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            pb['name'] = new[0]
            pb['phone'] = new[1]
            pb['comment'] = new[2]
            self.phone_book.append(pb)
        print('\n Телефонная книга загружена\n')

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        print(f'\nКонтакт {contact.get("name")} добавлен\n')

    def search(self, word: str) -> list:
        search_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result


    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value


    def delete_contact(self, i: int):
        contact = self.phone_book.pop(i)
        print(f'Контакт {contact.get("name")} удален')


    def save(self):
        with open(self.path, 'r') as data:
            old_data = data.read()
        with open(self.path, 'w') as new:
            new.write(old_data)


