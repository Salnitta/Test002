# ЗАДАЧА 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Введите день недели: '))

# if 0 < day < 8:
#     if day > 5:
#         print('Выходной')
#     else:
#         print('Будни')
# else:
#     print('Ты что-то не то ввел')


# ЗАДАЧА 3: Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой расположена эта точка (или на какой оси она расположена).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x, y = input('Введите координаты через пробел: ').split()
# x, y = int(x), int(y)
# if x > 0 and y > 0:
#     print('Первая четверть')
# elif x < 0 and y > 0:
#     print('Вторая четверть')
# elif x < 0 and y < 0:
#     print('Третья четверть')
# elif x > 0 and y < 0:
#     print('Четвертая четверть')
# else:
#     print('Одна из точек лежит на оси')


# ЗАДАЧА 4: Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# choice = int(input('Введите номер четверти: '))

# New Solution

# match choice:
#     case 1:
#         print('x > 0, y > 0')
#     case 2:
#         print('x < 0, y > 0')
#     case 3:
#         print('x < 0, y < 0')
#     case 4:
#         print('x > 0, y < 0')
#     case _:
#         print('Такой четверти нет')

# Classic Solution 

# if choice == 1:
#     print('x > 0, y > 0')
# elif choice == 2:
#     print('x < 0, y > 0')
# elif choice == 3:
#     print('x < 0, y < 0')
# elif choice == 4:
#     print('x > 0, y < 0')
# else:
#     print('Такой четверти нет')


# ЗАДАЧА 5: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math

# first = input('Введите координаты точки А через пробел: ').split()
# second = input('Введите координаты точки B через пробел: ').split()

# distance = (float(first[0]) - float(second[0]))**2 + (float(first[1]) - float(second[1]))**2
# print(f'Расстояние между точками = {round(math.sqrt(distance), 2)}')


# ЗАДАЧА 2: Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            flag = not(x or y or z) == (not x and not y and not z)
            print(f'{x, y, z} -> {flag}')
if flag:
    print('Выражение истинно при любом значении')
else:
    print('Условие не выполнено')