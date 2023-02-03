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
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    print()
    while True:
        try:
            choice = int(input('Выберите пункт меню: ')) 
            print()
            return choice
        except:
            print()
            input_error()
            
    

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('ТЕЛЕФОННАЯ КНИГА ПУСТА ИЛИ НЕ ОТКРЫТА')
        print()
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()

def input_error():
    print('ОШИБКА ВВОДА. ВВЕДИТЕ КОРРЕКТНЫЙ ПУНКТ МЕНЮ')
    print()

def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    print()
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    print()
    return find

def select_contact(phone_list: list, command: str):
    if len(phone_list) < 1:
        print('ТЕЛЕФОННАЯ КНИГА ПУСТА ИЛИ НЕ ОТКРЫТА')
        print()
    else:
        id_contact = int(input(f'Чтобы {command}, введите его номер: '))    # нужна проверка на int и наличие такого номера
        print()
        print(f'Вы хотите {command}: {phone_list[id_contact - 1][0]} {phone_list[id_contact - 1][1]} {phone_list[id_contact - 1][2]}')
        confirm = input(f'Нажмите 1 для подтверждения или Enter для отмены: ')
        print()
        if confirm:
            return int(id_contact)
    
    
def change_contact(phone_list: list, id_contact: int):
        print('Введите новые данные или нажмите Enter, чтобы пропустить: ')
        name = input(f'Текущие имя и фамилия: {phone_list[id_contact - 1][0]}\nНовые имя и фамилия: ')
        phone = input(f'Текущий телефон: {phone_list[id_contact - 1][1]}\nНовый телефон: ')
        comment = input(f'Текущий комментарий: {phone_list[id_contact - 1][2]}\nНовый комментарий: ')
        print()
        return name, phone, comment

def informing(message: str):
    print(message)
    print()











