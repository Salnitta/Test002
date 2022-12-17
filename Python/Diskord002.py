# my_list = [1,2,3,445,5]                    # cписок (изменяемый, индексируемый, динамический)
# my_tuple = (1,2,3,44,5,6,6)                # кортеж (неизменяемый)
# my_set = {1,2,3,344,55,6,67,8}             # множество (неиндексируемое, дубликатов нет, измененяемое)
# my_set2 = {2,3,55,6}
# my_dict = {'1':'one', (1,2,4):'two', 3:'three'}  # словарь (пара "ключ - значение", ключи уникальные)
# my_dict2 = {'1':'888', (1,2,4):'двойка', 7:'seven'} 


# print(my_set.difference(my_set2))          # разность множеств
# my_set.update(my_set2)                     # объединение множеств (без дубликатов)
# my_set.add(90)                             # добавление элемента
# my_set.remove(344)                         # удаление элемента множества

# new_list = list(my_set)                    # перевод множества в список

# print(my_dict.get('1'))
# print(my_dict.get(1,2,4))

# print(my_dict['1'])                        # аналог обращения по ключу (get), но будет ошибка, если нет такого ключа, поэтому всегда get
# print(my_dict.get(43, 'такого значения нет')) # после запятой сообщение, если такого ключа нет (вместо none)

# my_dict['new key'] = 'Мы добавили новый ключ' # добавление нового ключа и его значения в словарь
# my_dict['new key'] = 'Мы обновили новый ключ' # обновление значения ключа

# my_dict.update(my_dict2)                      # обновление одного словаря другим
# print(my_dict)

# keys = set()                                  # метод обнолвения одного словаря другим
# for i in my_dict:
#     keys.add(i)
# print(keys)
# for i in my_dict2:
#     keys.add(i)
# print(keys)

# new_dict = {}                                 # метод сложения/вычитания значений в двух словарях по ключу. Если значения int, то убираем str и вместо кавычек 0
# for i in keys:
#     new_dict[i] = str(my_dict.get(i, '')) + str(my_dict2.get(i, ''))
# print(my_dict)
# print(my_dict2)
# print(new_dict)

# my_dict.update(my_dict2)
# for i in my_dict.values:                         # проход по значениям .values
#     print(i)

# for k, v in my_dict.items():                     # проход по значениям и ключам .items
#     if v > 5:
#         print(k, v)

# people_id = {}
# people_id[1] = {'name': 'STONE', 'age': 38, 'comment': 'молоодец'}
# people_id[2] = {'name': 'Андрей Беляев', 'age': 18, 'comment': 'еще больше молоодец'}
# people_id[2] = {'name': 'Kol4an', 'age': 22, 'comment': 'он изучает языки'}      # перезапись элементов
# print(people_id)  
# print(people_id.get(1).get('name'))              # STONE
# print(people_id.pop(1))                          # удаление элемента

# ЗАЩИТА ОТ ДУРАКА

# def input_day():
#     while True:
#         try:
#             day = int(input('Введите день недели: '))
#             if 0 < day < 8:
#                 return day
#             else:
#                 print('Такого дня недели нет')
#         except:
#             print('Ну просили же ввести цифру, а ты?') # защита от ввода текста

# week_day = input_day()

# ЗАЩИТА ОТ ДУРАКА через регулярные выражения (email)

# import re

# pat = re.compile("[A-Za-z0-9]*@[A-Za-z0-9]*.[a-z]{2,5}")
# print(pat.findall("andrew107021@gmail.com"))

# ЦИКЛЫ

# from pprint import pprint


# my_list = [234,53,3465,45,745,7]

# for item in my_list:    # перебор значений (не индексов)
#     print(item)

# for item in range(0, 10, 1):  # перебор по индексам (начальное значение, конечное значение, не включительно, шаг)
#     print(item)

# for item in range(len(my_list)):
#     print(my_list[item])

# # бесконечный цикл # while True:

# i = 8
# while i < 10:
#     print(i)
#     i += 1

# for i in my_list:        # вариант бесконечного цикла на for
#     my_list.append(7)

# for i in my_list:                 # Блок else для for (после выполнения цикла до конца, но если цикл остановится, то else не сработает
#     print(i)
# else:
#     print('Проход по списку окончен')

# for i in my_list:
#     if i < 10:
#         print(i)
#         break
# else:
#     print('Однозначных числе в списке нет')


# flag = True                        # альтернативное решение без else
# for i in my_list:
#     if i < 10:
#         print(i)
#         flag = False
#         break

# if flag:
#     print('Однозначный чисел в списке нет')

# my_num = 1  # 0, none, False, [], '' - не сработает, остальное сработает

# if my_num:
#     print('Сработало')

# number = 10

# if number > 0:
#     print('Сработало')
# elif number > 5:
#     print('Сработал ELIF')
# else:
#     print('Сработал ELSE')

my_list = [1, 44, 5, 34, 77, 5, 5, 77]
print(my_list.count(5))                           # счетчик

def my_count(my_list: list, number: int) -> int:  # функция - аналог счетчика 
    count = 0
    for i in my_list:
        if i == number:
            count += 1
    return count

print(my_count(my_list, 5))