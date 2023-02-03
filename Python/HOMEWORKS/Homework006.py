# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Классический вариант решения:

# num = input('Введите число: ')

# res = 0
# for char in num:
#     if char.isdigit():
#         sum += int(char)

# print(f'{num} -> {res}')

# Решение через функции:

# print(num := input('Введите число: '), '->', sum(list(map(int, [char for char in num if char.isdigit()]))))


# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# Классический способ решения

# n = int(input('Введите n: '))
# n_list = []
# sum = 0
# for i in range(1, n + 1):
#     n_list.append(round((1 + 1 / i) ** i, 2))
# for item in n_list:
#     sum += item
# print(f'Для n = {n} -> {n_list}\nСумма = {sum}')

# Решение через функции:

# print('Для n =', n := int(input('Введите n: ')), '->', n_list := [round((1 + 1 / i) ** i, 2) for i in range(1, n + 1)], '\nCумма =', sum(n_list))

# import random

# Классическое решение

# def create_list():
#     new_list = []
#     for i in range(10):
#         new_list.append(i)
#     return new_list

# def my_shuffle(my_list: list):    
#     new_list = []
#     while len(my_list) > 0:
#         ni = random.randint(0, len(my_list) - 1)
#         new_list.append(my_list.pop(ni))
#     return new_list

# my_list = create_list()
# print(my_list)
# print(my_shuffle(my_list))

# Решение через функции

# print('Исходный список:', (ml := [i for i in range(15)]).copy(), '\nПеремешанный список:',\
    #    sl := [ml.pop(random.randint(0, len(ml) - 1)) for i in range(len(ml))])


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

# Классическое решение

# def create_list() -> list:
#     n = RI(5, 10)
#     initial_list = []
#     for i in range(n):
#         initial_list.append(RI(1, 7))
#     return initial_list

# def odd_elements_sum(new_list: list):
#     sum = 0
#     for i in range(1, len(new_list), 2):
#         sum += new_list[i]
#     return sum

# original_list = create_list()
# result = odd_elements_sum(original_list)
# print(f'{original_list} -> сумма элементов на нечетных позициях = {result}')


# Решение через функцию

print(orig_list := [RI(1, 7) for i in range(RI(5, 10))], '-> сумма элементов на нечетных позициях =',\
       sum([orig_list[i] for i in range(1, len(orig_list), 2)]))
