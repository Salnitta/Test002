# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы


import view
import model

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:
            case 1:
                message = model.open_file()
                view.informing(message)
            case 2:
                message = model.save_file()
                view.informing(message)
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                message = model.add_new_contact(new_contact)
                view.informing(message)
            case 5:
                id_contact = view.select_contact(model.get_phone_book(), 'удалить контакт')
                if id_contact:
                    message = model.delete_contact(id_contact)
                    view.informing(message)
            case 6:
                id_contact = view.select_contact(model.get_phone_book(), 'изменить контакт')
                if id_contact:
                    changed_contact = list(view.change_contact(model.get_phone_book(), id_contact))
                    message = model.update_contact(changed_contact, id_contact)
                    view.informing(message)
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                view.informing('ПРОГРАММА ЗАВЕРШЕНА')
            case _:
                view.input_error()
            
