# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = input('Введите число: ')
# new_number = number.replace(',', '').replace('.', '')
# result = 0
# for item in new_number:
#     result += int(item) 
# print(f'{number} -> {result}')

# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите n: '))
# n_list = []
# sum = 0
# for i in range(1, n + 1):
#     n_list.append(round((1 + 1 / i) ** i, 2))
# for item in n_list:
#     sum += item
# print(f'Для n = {n} -> {n_list}\nСумма = {sum}')

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

def shuffle_list(original_list: list) -> list:
    k = 1
    for i in range(len(original_list) - 1):
        ri = random.randint(k, len(original_list) - 1)
        temp = original_list[i]
        original_list[i] = original_list[ri]
        original_list[ri] = temp
        k += 1
    return(original_list)

n = int(input('Введите количество элементов списка: '))
n_list = []
for i in range(n):
    n_list.append(i)
print(n_list)
print(shuffle_list(n_list))

