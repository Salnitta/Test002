# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

phone_book = []
path = 'SEMINARS/SEMINAR007/data.txt'

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
    message = 'ФАЙЛ ОТКРЫТ'
    return message
    

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)
    message = 'СОЗДАН НОВЫЙ КОНТАКТ'
    return message


def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result


def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open (path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))
    message = 'ФАЙЛ СОХРАНЕН'
    return message


def delete_contact(id_contact: int):
    global phone_book
    phone_book.pop(id_contact - 1)
    message = 'КОНТАКТ УДАЛЕН'
    return message


def update_contact(changed_contact: list, id_contact: int):
    global phone_book
    for i, item in enumerate(changed_contact):
        if item:
            phone_book[id_contact - 1][i] = item
    message = 'КОНТАКТ ИЗМЕНЕН'
    return message
 









