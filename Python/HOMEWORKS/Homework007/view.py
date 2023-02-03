# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu() -> int:
    print('\nГлавное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choice = int(input('\nВыберите пункт меню: ')) 
            if 0 < choice < 9:
                return choice
            else:
                print('\nВВЕДИТЕ ЦИФРУ ОТ 1 ДО 8')
        except:
            input_error()
            

def input_error():
    print('\nОШИБКА ВВОДА. ВВЕДИТЕ НОМЕР ПУНКТА МЕНЮ')


def informing(message: str):
    print(message)
      

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('\nТЕЛЕФОННАЯ КНИГА ПУСТА ИЛИ НЕ ОТКРЫТА')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
    

def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def select_contact(message: str):
    contact = input(message)
    print()
    return contact


def show_find_contacts(contact_list: list):
    for contact, id in contact_list:
            print(f'\t{id + 1}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')


def confirm(contact: str, command: str):
    print(f'Вы действительно хотите {command} {contact}?')
    while True:
        try:
            confirm = input(f'Нажмите 1 для подтверждения или Enter для отмены: ')
            if confirm not in {'1', ''}:
                print('Некорректный ввод')
            elif confirm:
                return True
            else:
                print('\nОТМЕНЕНО')
                return False
        except:
            print('Некорректный ввод')


def change_contact(contact: list):
        print('Введите новые данные или нажмите Enter, чтобы пропустить: ')
        name = input(f'Текущие имя и фамилия: {contact[0]}\nНовые имя и фамилия: ')
        phone = input(f'Текущий телефон: {contact[1]}\nНовый телефон: ')
        comment = input(f'Текущий комментарий: {contact[2]}\nНовый комментарий: ')
        return name, phone, comment














