# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

file = []

def init(value):
    if value == 1:
        open_file()
    elif value == 2:
        save_file()
    elif value == 3:
        show_contacts()
    elif value == 4:
        create_contact()
    elif value == 5:
        delete_contact()
    elif value == 6:
        change_contact()
    elif value == 7:
        find_contact()
    elif value == 8:
        exit()
    else:
        print('Некорректный ввод данных')
             

def open_file():
    path = 'SEMINARS/SEMINAR007/data.txt'
    with  open (path, 'r') as data:
        file = data.read().split('\n')
    print('Файл открыт')
    return file

def show_contacts():
    print(file)



