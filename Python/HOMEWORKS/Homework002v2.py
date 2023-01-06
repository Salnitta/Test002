# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input('Введите число: ')

# sum = 0
# for char in num:
#     if char.isdigit():
#         sum += int(char)

# print(sum)

# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# num = int(input('Введите целое число: '))

# my_list = []

# for n in range(1, num + 1):
#     number = round((1+1/n)**n, 2)
#     my_list.append(number if number != int(number) else int(number))

# print(f'При n = {num} список -> ', end='')
# print(*my_list, sep=', ')
# print(f'И его сумма -> {sum(my_list)}')

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

def create_list():
    new_list = []
    for i in range(10):
        new_list.append(i)
    return new_list

# def my_shuffle(my_list: list):    # первый вариант метода
#     ni = random.randint(0, len(my_list) - 1)
    # for i in range(len(my_list)):
    #     my_list[i], my_list[ni] = my_list[ni], my_list[i]
    # return my_list

def my_shuffle(my_list: list):    # второй более оптимальный вариант метода
    new_list = []
    while len(my_list) > 0:
        ni = random.randint(0, len(my_list) - 1)
        new_list.append(my_list.pop(ni))
    return new_list

my_list = create_list()
print(my_list)
print(my_shuffle(my_list))




