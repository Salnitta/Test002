# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.

# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# Решение в группе через словарь

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_dict = {}
# new_list = []

# for i in range(len(my_list)):
#     my_dict[my_list[i]] = my_dict.get(my_list[i], 0) + 1
# print(my_dict)

# for key, item in my_dict.items():
#     if item == 1:
#         new_list.append(key)
# print(new_list)

# Решение преподавателя через функцию count

# import random

# my_list = [random.randint(0, 10) for _ in range(15)] 
# print(my_list)

# new_list = [x for x in my_list if my_list.count(x) == 1]
# print(new_list)


# 2. Напишите программу вычисления арифметического выражения 
# заданного строкой. Используйте операции +,-,/,*. приоритет 
# операций стандартный. 
    
#     *Пример:*     
#     2+2 => 4;    
#     1+2*3 => 7;     
#     1-2*3 => -5;

# Решение в группе (не на всех примерах удачно отрабатывает, например, если добавить + 1 в конце)

# my_str = '1+2*3 - 10 /5 + 1'
# result = 0
# my_str = my_str.replace(' ', '').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split(' ')
# print(my_str)

# i = 0
# while i < len(my_str):
#     if my_str[i] == '*':
#         my_str[i - 1] = int(my_str[i - 1]) * int(my_str[i + 1])
#         del my_str[i]
#         del my_str[i]
#     i += 1
# print(my_str)

# i = 0
# while i < len(my_str):
#     if my_str[i] == '/':
#         my_str[i - 1] = int(my_str[i - 1]) / int(my_str[i + 1])
#         del my_str[i]
#         del my_str[i]
#     i += 1
# print(my_str)

# i = 0
# while i < len(my_str):
#     if my_str[i] == '+':
#         my_str[i - 1] = int(my_str[i - 1]) + int(my_str[i + 1])
#         del my_str[i]
#         del my_str[i]
#     i += 1
# print(my_str) 

# i = 0      
# while i < len(my_str):
#     if my_str[i] == '-':
#         my_str[i - 1] = int(my_str[i - 1]) - int(my_str[i + 1])
#         del my_str[i]
#         del my_str[i]
#     i += 1
# print(my_str) 

# Решение преподавателя (классический код):

# input_data = input('Введите выражение: ')
# # input_data = '-  1+  2* 3 - 10/ 5 + 1'

# input_data = input_data.replace(' ', '').replace('*', ' * ').replace('/', ' / ')\
#         .replace('+', ' + ').replace('-', ' - ')

# if input_data.startswith(' - '):
#     input_data = '-' + input_data[3:]

# example = input_data.split(' ')

# # while len(example) > 1:
# while '*' in example or '/' in example:
#         i = 0
#         while i < len(example):
#             if example[i] == '*':
#                 example[i - 1] = int(example[i - 1]) * int(example[i + 1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] == '/':
#                 example[i - 1] = int(example[i - 1]) / int(example[i + 1])
#                 example.pop(i)
#                 example.pop(i)
#             else:
#                 i += 1
# while '+' in example or '-' in example:
#         i = 0
#         while i < len(example):
#             if example[i] == '+':
#                 example[i - 1] = int(example[i - 1]) + int(example[i + 1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] == '-':
#                 example[i - 1] = int(example[i - 1]) - int(example[i + 1])
#                 example.pop(i)
#                 example.pop(i)
#             else:
#                 i += 1

# print(f'{input_data} = {example[0]}')


# Решение преподавателя (с применением функций):

input_data = input('Введите выражение: ')

input_data = input_data.replace(' ', '').replace('*', ' * ').replace('/', ' / ')\
        .replace('+', ' + ').replace('-', ' - ')

if input_data.startswith(' - '):
    input_data = '-' + input_data[3:]

example = input_data.split(' ')

operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}

def calculate(operator_1, operator_2):
    i = 0
    while operator_1 in example or operator_2 in example:
        if example[i] in [operator_1, operator_2]:
            example[i - 1] = operation.get(example[i])(int(example[i - 1]), int(example[i + 1]))
            example.pop(i)
            example.pop(i)
        else:
             i += 1

while len(example) > 1:
     calculate('*', '/')
     calculate('+', '-')

print(f'{input_data} = {example[0]}')

    














