# Теоретическая часть

# my_string = '\tПитон самый лучший в мире язык\n'
# new_string = my_string.split() # делит строку по указанному символу, по умолчанию пробел, на выходе получаем уже не строку, а список
# print(my_string)
# print(new_string)
# new_string = my_string.replace('и', '$').replace('п', '!!!') # заменяет символы
# print(new_string)
# new_string = my_string.strip() # убирает табуляции и лишние пробелы в начале и конце
# new_string = my_string.lstrip() # чистит слева
# new_string = my_string.rstrip() # чистит справа
# if my_string.lower().startswith('пит'): # проверка, с чего начинается # lower переводит в нижний регистр
#     print('Да, все верно')
# if my_string.endswith('зык'): # проверка, на что заканчивается
#     print('Да, все верно') 
# print(my_string.upper()) # upper переводит в верхний регистр

# my_list = ['23', 'gh', '655', '788']
# add = '-ss'
# print(add.join(my_list)) # склеивает список строк через выбранный символ
# print(' '.join(my_list))

# my_dict = {32:'23', 1:'Один', 3:45, 'Ключ': 2132323, 'Список': [12, 34, 56, 343]}
# print(my_dict(1))
# print(my_dict.get(2, 'Нет такого ключа'))
# print(my_dict.get(3, 0))
# print(my_dict.get(2, 0) + my_dict(3, 0))
# my_dict['New'] = 'value'
# print(my_dict)
# my_dict['32'] = 'value' # если такой ключ уже есть, значение перезаписывается
# my_dict[3] = my_dict.get(3) + 1 # увеличили значение на 1

# Задача - посчитать количество разных цифр в строке

# my_dict = {}

# num_list = '23565654663847875898397662534254324556'
# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1
# print(my_dict)

# Задача 2: Задано квадратное уравнение типа 'A*x**2 + B*x + C = 0', нужно написать алгоритм, 
# который получит коэффиценты из уравнения, и посчитать X

# Решение в группе (вычислить дискриминант не успели):

# def conv(my_str):
#     new_str = my_str.split('x')
#     print(new_str)
#     new_str2 = []
#     for i in range(len(new_str)):
#         new_str2.append(new_str[i].replace('**2', '').replace('*', '')\
#             .replace(' ', '').replace('+', '').replace('=', '').replace('0', ''))
#     return new_str2

# stringa = '32*x**2 + 4*x - 6 = 0'
# str_new = conv(stringa)
# for i in range(3):
#     str_new[i] = int(str_new[i])
# print(str_new)

# Решение преподавателя:

# import math

# equation = '6 *x**2  + 4*x -3 = 0'

# def create_koef(equation: str) -> tuple:
#     new_coef = []
#     nq = equation.replace(' ', '').replace('=0', '').\
#         replace('+', ' ').replace('-', ' -').split()
#     # print(nq)
#     for item in nq:
#         if item.startswith('x'):
#             new_coef.append(1)
#         elif item.startswith('-x'):
#             new_coef.append(-1)
#         else:
#             new_coef.append(int(item.split('*x')[0]))
#     return new_coef

# def solution(koef: list):
#     a, b, c = koef
#     disc = b**2 - 4*a*c
#     if disc > 0:
#         x1 = (-b + math.sqrt(disc))/(2*a)
#         x2 = (-b - math.sqrt(disc))/(2*a)
#         return 2, round(x1, 2), round(x2, 2)  # всегда возвращаем кортеж из 3х элементов
#     elif disc == 0:                           # 1ый элемент означает сколько корней
#         x = -b//(2*a)
#         return 1, round(x, 2), None           # всегда возвращаем кортеж из 3х элементов
#     else:                                     # 1ый элемент означает сколько корней
#         return 0, None, None                  # всегда возвращаем кортеж из 3х элементов
#                                               # 1ый элемент означает сколько корней
# print(solution(create_koef(equation)))        # нужна еще проверка деления на 0


# Домашнее задание

import random

k = int(input('Введите максимальную степень: '))
equation = {}
for i in range(k, -1, -1):
    equation[i] = random.randint(0, 100)

print(equation)

eq_str = ''
for k, v in equation.items():
    if k == 1:
        eq_str += f'{v}*x + '
    elif k == 0:
        eq_str += f'{v} + '
    else:
        eq_str += f'{v}*x**{k} + '
eq_str = eq_str[:-3]

print(eq_str)