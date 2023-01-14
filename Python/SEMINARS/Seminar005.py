# ТЕОРИЯ

# from random import randint as RI

# my_list = []
# for x in range(10):
#     my_list.append(x)

# print(my_list)

# my_list = [x for x in range(10) if x % 2 != 0]
# print(my_list)

# my_list = [RI(0, 10) for x in range(10)]
# print(my_list)

# def pow(x):
#     return x**2

# my_list = [pow(x) for x in range(10)]
# print(my_list)

# my_list = [x**2 for x in range(10)]
# print(my_list)

# my_list = {x: x**2 for x in range(10)} # dictionary
# print(my_list)

# my_list = [x for x in range(10)]
# my_list = list(map(str, my_list))

# print(my_list)


# for i in range(len(my_list)):
#     my_list[i] = str(my_list[i])

# print(my_list)

# my_list = '23 6 45 8989 45 333 909 674 44'
# my_list = list(filter(lambda x: not '4' in x, my_list.split()))
# print(my_list)

# my_list = '23 6 45 8989 45 333 909 674 44'
# my_list = list(filter(lambda x: x%2 == 0, list(map(int, my_list.split()))))
# print(my_list)

# my_list = '23 6 45 8989 45 333 909 674 44'
# my_list = my_list.split()
# print(my_list)

# for i, item in enumerate(my_list, 5): # можно задать первое значение
#     print(i, item)

# my_list_1 = '23 6 45 8989 45 333 909 674 44'.split()
# my_list_2 = [124, 5, 454, 5656, 78, 787, 67, 78, 9]

# print(list(zip(my_list_1, my_list_2))) # объединяет списки в кортеж, может быть несколько списков, больше двух

# my_list_1 = 'Иван Мария Петр'.split()
# my_list_2 = 'Иванов Пухальская Игнатьев'.split()
# my_list_3 = (232323, 454545, 565665)
# print(list(zip(my_list_1, my_list_2, my_list_3)))

# def power(x):
#     return x**2

# func = lambda x: x**2
# print(func(4))

# def print_smile(name):
#     print(f'{name}, smile')

# on_click = lambda name: print_smile(name)

# on_click('Kirill')


# def comparison(x):
#     return x > 0

# my_list = [x for x in range(-10, 10)]
# print(my_list)

# print(list(filter(comparison, my_list))) # через функцию

# print(list(filter(lambda x: x > 0, my_list))) # через lambda


# ПРАКТИКА

# 1.Напишите программу, удаляющую из текста все слова, содержащие 'абв'

# string = 'Питон - пожабвлуй лучший из худабвших языков в мире'

# var 0 - по-старому:
# string = string.split()
# new_list = []
# for word in string:
#     if not 'абв' in word:
#         new_list.append(word)

# print(' '.join(new_list))

# var 1:
# # string = str.split()
# new_list = list(filter(lambda word: not 'абв' in word, string.split()))
# print(' '.join(new_list))

# var 2:
# new_list = [x for x in string.split() if not 'абв' in x]
# print(new_list)
# print(' '.join(new_list))

# 2. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найдите это число.

# var 1 - универсальный:
# path = r'SEMINARS/file.txt' # r позволяет избежать ошибок с путем

# with open(path, 'r') as data:
#     text = data.read().split()

# my_list = list(map(int, text))
# print(my_list)

# my_list = [my_list[x]-1 for x in range(1, len(my_list)) if my_list[x] - 1 != my_list[x-1]]
# print(my_list)

# var 2 - если не хватает одного числа:

# path = r'SEMINARS/file.txt' # r позволяет избежать ошибок с путем

# with open(path, 'r') as data:
#     text = data.read().split()

# my_list = list(map(int, text))
# # true_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# true_list = [x for x in range(1, len(my_list))]
# print(my_list)

# new_list = list(zip(my_list, true_list))
# print(new_list)

# for item in new_list:
#     if item[0] != item[1]:
#         print(item[1])
#         break

# Библиотека tkinter для крестиков - ноликов
# import tkinter as tk





