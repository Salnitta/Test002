# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

phone_book = []
path = 'HOMEWORKS/Homework007/data.txt'

def get_phone_book():
    global phone_book
    return phone_book


def open_file():
    global phone_book
    global path
    with open (path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open (path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))


def search_contact(text: str):
    global phone_book
    result = []
    for i, contact in enumerate(phone_book):
        for field in contact:
            if text in field:
                result.append((contact, i))
                break
    return result


def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)


def delete_contact(contact: list):
    global phone_book
    phone_book.remove(contact)


def update_contact(changed_contact: list, id_contact: int):
    global phone_book
    for i, item in enumerate(changed_contact):
        if item:
            phone_book[id_contact][i] = item
 









