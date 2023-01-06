# ЗАДАЧА 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Введите номер дня недели: '))
# if day > 7 or day < 1:                    # 0 < day < 8
#     print('Введенное число не соответствует ни одному дню недели')
# elif day == 6 or day ==7:
#     print('Да, выходной')
# else:
#     print('Нет, будний день')


# ЗАДАЧА 2: Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('Введите значения предикат для проверки истинности утверждения:')
# print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# X = int(input('X = '))
# Y = int(input('Y = '))
# Z = int(input('Z = '))
# if (X == 0 or X == 1) and (Y == 0 or Y == 1) and (Z == 0 or Z == 1):
#     bool1 = not (X or Y or Z)
#     bool2 = (not X) and (not Y) and (not Z)
#     result = bool1 == bool2
#     if result:
#         print('Для введенных значений предикат утверждение истинно')
#     else:
#         print('Для введенных значений предикат утверждение ложно')
# else:
#     print('Введены недопустимые значения предикат')


# ЗАДАЧА 3: Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой расположена эта точка (или на какой оси она расположена).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print('Введите координаты точки, чтобы узнать ее расположение на плоскости:')
# X = float(input('X = '))
# Y = float(input('Y = '))
# if X == 0 and Y != 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) принадлежит оси Х')
# elif Y == 0 and X != 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) принадлежит оси Y')
# elif X == 0 and Y == 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) расположена в центре координатной плоскости')
# elif X > 0 and Y > 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) расположена в четверти 1')
# elif X < 0 and Y > 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) расположена в четверти 2')
# elif X < 0 and Y < 0:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) расположена в четверти 3')
# else:
#     print(f'ОТВЕТ: Точка с координатами ({X}; {Y}) расположена в четверти 4')

# ЗАДАЧА 4: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input('Введите номер четверти плоскости: '))
# if number < 1 or number > 4:
#     print('Такой четверти не существует')
# elif number == 1:
#     print('Диапазон возможных координат: X > 0, Y > 0')
# elif number == 2:
#     print('Диапазон возможных координат: X < 0, Y > 0')
# elif number == 3:
#     print('Диапазон возможных координат: X < 0, Y < 0')
# else:
#     print('Диапазон возможных координат: X > 0, Y < 0')

# ЗАДАЧА 5: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# print('Введите координаты двух точек:')
# x1 = float(input('x1 = '))
# y1 = float(input('y1 = '))
# x2 = float(input('x2 = '))
# y2 = float(input('y2 = '))
# length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# print(f'Расстояние между точками = {round(length, 2)}')


# ЗАДАЧА 2: Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            bool = not (X or Y or Z) == (not X and not Y and not Z)
            print(f'{X, Y, Z} - {bool}')
