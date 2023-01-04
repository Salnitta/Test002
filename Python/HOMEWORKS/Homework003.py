# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# def create_list() -> list:
#     n = random.randint(5, 10)
#     initial_list = []
#     for i in range(n):
#         initial_list.append(random.randint(1, 7))
#     return initial_list

# def odd_elements_sum(new_list: list):
#     sum = 0
#     for i in range(1, len(new_list), 2):
#         sum += new_list[i]
#     return sum

# original_list = create_list()
# result = odd_elements_sum(original_list)
# print(f'{original_list} -> сумма элементов на нечетных позициях = {result}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random

# def create_list() -> list:
#     n = random.randint(5, 10)
#     initial_list = []
#     for i in range(n):
#         initial_list.append(random.randint(1, 7))
#     return initial_list

# def pairs_multiplication(initial_list: list) -> list:
#     result_list = []
#     n = len(initial_list)//2
#     l = len(initial_list) - 1
#     for i in range (n):
#         result_list.append(initial_list[i] * initial_list[l])
#         l -= 1
#     if len(initial_list) % 2 != 0:
#         result_list.append(initial_list[n]**2)
#     return result_list

# given_list = create_list()
# recieved_list = pairs_multiplication(given_list)
# print(f'{given_list} => {recieved_list}')


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# def create_float_list() -> list:
#     l = random.randint(5, 10)
#     new_list = []
#     for i in range(l):
#         new_list.append(round(random.uniform(1, 10), 2))
#     return new_list

# def fractional_separation(available_list: list) -> list:
#     obtained_list = []
#     for item in available_list:
#         if item != int(item):
#             obtained_list.append(round(item - int(item), 2))
#     return obtained_list

# def minimax(search_list: list):
#     max = search_list[0]
#     min = search_list[0]
#     for i in range(1, len(search_list)):
#         if search_list[i] > max:
#             max = search_list[i]
#         elif search_list[i] < min:
#             min = search_list[i]
#     return (min, max)


# initial_list = create_float_list()
# result_list = fractional_separation(initial_list)
# min, max = minimax(result_list)
# diff = round(max - min, 2)
# print(f'{initial_list}\nРазница между максимальной ({max}) и минимальной ({min}) дробной частью = {diff}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# РЕШЕНИЕ ЧЕРЕЗ СТРОКУ
# dec = int(input('Введите десятичное число: '))
# bin = ''
# while dec >= 2:
#     bin = str(dec % 2) + bin
#     dec = dec // 2
# bin = str(dec) + bin
# print(bin)

# РЕШЕНИЕ МАТЕМАТИЧЕСКИМ СПОСОБОМ
# dec = int(input('Введите десятичное число: '))
# bin = 0
# k = 1
# while dec >= 2:
#     if dec % 2 != 0:
#         bin += dec % 2 * k
#     dec = dec // 2
#     k *= 10
# if dec != 0:
#     bin += dec * k
# print(bin)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
# (Негафибоначчи).
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def negafib(n):
    if n == 0:
        return 0
    elif n == -1:
        return 1
    else:
        return negafib(n+2) - negafib(n+1)


n = int(input('Введите число: '))
fibonacci = []
for e in range (-n, n+1):
    if e < 0:
        fibonacci.append(negafib(e))
    else:
        fibonacci.append(fib(e))
print(fibonacci)








