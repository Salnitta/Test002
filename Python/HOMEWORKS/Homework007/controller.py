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
                model.open_file()
                view.informing('\nФАЙЛ ОТКРЫТ')

            case 2:
                model.save_file()
                view.informing('\nФАЙЛ СОХРАНЕН')

            case 3:
                view.informing('\nВСЕ КОНТАКТЫ:')
                view.show_contacts(model.get_phone_book())

            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.informing('\nСОЗДАН НОВЫЙ КОНТАКТ')

            case 5:
                select = view.select_contact('Введите удаляемый контакт: ')
                contact = model.search_contact(select)
                if len(contact) == 1:
                    confirm = view.confirm(contact[0][0][0], 'удалить контакт')
                    if confirm:
                        model.delete_contact(contact[0][0])
                        view.informing('\nКОНТАКТ УДАЛЕН')
                elif contact == []:
                    view.informing('КОНТАКТ НЕ НАЙДЕН')
                else:
                    view.informing('НАЙДЕНО НЕСКОЛЬКО КОНТАКТОВ:')
                    view.show_find_contacts(contact)
                    view.informing('\nВВЕДИТЕ БОЛЕЕ ТОЧНЫЕ ДАННЫЕ')

            case 6:
                select = view.select_contact('Введите изменяемый контакт: ')
                contact = model.search_contact(select)
                if len(contact) == 1:
                    changed_contact = view.change_contact(contact[0][0])
                    model.update_contact(changed_contact, contact[0][1])
                    view.informing('\nКОНТАКТ ИЗМЕНЕН')
                elif contact == []:
                    view.informing('КОНТАКТ НЕ НАЙДЕН')
                else:
                    view.informing('НАЙДЕНО НЕСКОЛЬКО КОНТАКТОВ:')
                    view.show_find_contacts(contact)
                    view.informing('\nВВЕДИТЕ БОЛЕЕ ТОЧНЫЕ ДАННЫЕ')

            case 7:
                find = view.select_contact('Введите искомый контакт: ')
                result = model.search_contact(find)
                if result == []:
                    view.informing('КОНТАКТ НЕ НАЙДЕН')
                else:
                    view.informing('НАЙДЕНЫ КОНТАКТЫ:')
                    view.show_find_contacts(result)

            case 8:
                view.informing('\nПРОГРАММА ЗАВЕРШЕНА\n')
            
