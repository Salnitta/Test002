# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# my_list = ['df32df', 'eyr1yi', '12fgh9h', '45ghg', '08gh7']
# print(my_list)
# search = input('Введите искомое число: ')
# for item in my_list:
#     if search in item:
#         print(f'Число {search} входит в заданный список')
#         break
# else:
#     print(f'Число {search} НЕ входит в заданный список')


# 3. Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# Решение мое:

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# my_list = ["123", "234", 123, "567"]
# my_list = []
# print(my_list)
# search = '123'
# count = 0
# for i in range(len(my_list)):
#     if search == my_list[i]:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)

# Решение через функцию:

# my_list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# my_list4 = ["123", "234", 123, "567"]

# def check(my_list: list, search):
#     count = 0
#     for i in range(len(my_list)):
#         if search == my_list[i]:
#             count += 1
#             if count == 2:
#                 print(f'Второй индекс вхождения - {i}')
#                 break
#     else:
#         print('Второго вхождения нет')

# check(my_list1, 'qwe')
# check(my_list2, 'йцу')
# check(my_list3, '123')
# check(my_list4, '123')

# Решение через встроенный метод index, но нужен обработчик ошибок на случай, если элемента в списке нет

# print(my_list1.index('qwe', 2)) 
# print(my_list2.index('йцу', 2))

# Как создать список вещественных чисел:

import random
my_list = []
for _ in range(10):
    amount = random.randint(0,3)
    number = round(random.uniform(-10, 10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)

print(my_list)