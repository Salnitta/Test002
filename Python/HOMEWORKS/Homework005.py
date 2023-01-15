# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется 
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# ИГРА ЧЕЛОВЕКА С ЧЕЛОВЕКОМ

# import random

# def check(min: int, max: int, name: str):
#     while True:
#         part = int(input(f'Возьми конфеты, {name}: '))
#         if min < part <= max:
#             return part
#         elif part < min:
#             print('Нельзя взять отрицательное число конфет')
#         elif part == 0: 
#             print('Нельзя пропускать ход')
#         else:
#             print(f'Можно взять не больше {max} конфет')

# def play(number: int, min: int, max: int, player_1: str, player_2: str) -> str:
#     while number > min:
#         number = taking_candy(number, min, max, player_1)
#         winner = 1
#         if number >= 1:
#             number = taking_candy(number, min, max, player_2)
#             winner = 0
#     if winner:
#         return player_1
#     else:
#         return player_2

# def taking_candy(number: int, min: int, max: int, name: str):
#     if number >= max:
#             part = check(min, max, name)
#             number -= part
#             print(f'Осталось конфет - {number}')
#     else:
#         part = check(min, number, name)
#         number -= part
#         print(f'Осталось конфет - {number}')
#     return number


# min = 0
# max = 28
# candy = random.randint(29, 200)
# print(f'На столе лежит: {candy} конфет')
# name_A = input('Введите имя первого игрока: ')
# name_B = input('Введите имя второго игрока: ')
# toss = random.randint(1, 2)
# if toss == 1:
#     print(f'Первый ход за игроком - {name_A}')
#     winner = play(candy, min, max, name_A, name_B)
# else:
#     print(f'Первый ход за игроком - {name_B}')
#     winner = play(candy, min, max, name_B, name_A)

# print(f'{winner} - победитель!')

    

# ИГРА ЧЕЛОВЕКА С БОТОМ (БЕЗ ИНТЕЛЛЕКТА)

# import random

# def check(min: int, max: int, name: str):
#     while True:
#         part = int(input(f'{name}, возьми конфеты: '))
#         if min < part <= max:
#             return part
#         elif part < min:
#             print('Нельзя взять отрицательное число конфет')
#         elif part == 0: 
#             print('Нельзя пропускать ход')
#         else:
#             print(f'Можно взять не больше {max} конфет')

# def play(number: int, min: int, max: int, toss: bool, bot: str, player: str) -> str:
#     while number > min:
#         if toss:
#             number = bot_step(number, min, max, bot)
#             winner = 1
#             if number >= 1:
#                 number = player_step(number, min, max, player)
#                 winner = 0
#         else:
#             number = player_step(number, min, max, player)
#             winner = 0
#             if number >= 1:
#                 number = bot_step(number, min, max, bot)
#                 winner = 1
#     if winner:
#         return bot
#     else:
#         return player

# def player_step (number: int, min: int, max: int, name: str):
#     if number >= max:
#         part = check(min, max, name)
#         number -= part
#         print(f'Осталось конфет - {number}')
#     else:
#         part = check(min, number, name)
#         number -= part
#         print(f'Осталось конфет - {number}')
#     return number

# def bot_step (number: int, min: int, max: int, name: str):
#     if number >= max:
#         part = random.randint(min + 1, max)
#         print(f'{name} взял конфет: {part}')
#         number -= part
#         print(f'Осталось конфет - {number}')
#     else:
#         part = random.randint(min + 1, number)
#         print(f'{name} взял конфет: {part}')
#         number -= part
#         print(f'Осталось конфет - {number}')
#     return number


# min = 0
# max = 28
# candy = random.randint(29, 200)
# name_A = 'Bot'
# print(f'Привет, я - {name_A}')
# name_B = input('Как тебя зовут? ')
# print(f'На столе лежит {candy} конфет')
# toss = random.randint(0, 1)
# if toss:
#     print(f'Первый ход за игроком - {name_A}')
# else:
#     print(f'Первый ход за игроком - {name_B}')
# winner = play(candy, min, max, toss, name_A, name_B)

# print(f'{winner} - победитель!') 



# ИГРА ЧЕЛОВЕКА С ИНТЕЛЛЕКТУАЛЬНЫМ БОТОМ

# import random

# def check(min: int, max: int, name: str):
#     while True:
#         part = int(input(f'{name}, возьми конфеты: '))
#         if min < part <= max:
#             return part
#         elif part < min:
#             print('Нельзя взять отрицательное число конфет')
#         elif part == 0: 
#             print('Нельзя пропускать ход')
#         else:
#             print(f'Можно взять не больше {max} конфет')

# def play(number: int, min: int, max: int, toss: bool, bot: str, player: str) -> str:
#     while number > min:
#         if toss:
#             number = bot_step(number, min, max, bot)
#             winner = 1
#             if number >= 1:
#                 number = player_step(number, min, max, player)
#                 winner = 0
#         else:
#             number = player_step(number, min, max, player)
#             winner = 0
#             if number >= 1:
#                 number = bot_step(number, min, max, bot)
#                 winner = 1
#     if winner:
#         return bot
#     else:
#         return player

# def player_step (number: int, min: int, max: int, name: str):
#     if number >= max:
#         part = check(min, max, name)
#         number -= part
#         print(f'Осталось конфет - {number}')
#     else:
#         part = check(min, number, name)
#         number -= part
#         print(f'Осталось конфет - {number}')
#     return number

# def bot_step (number: int, min: int, max: int, name: str):
#     if number >= max:
#         if number % 29 != 0:
#             part = number % 29
#         else: 
#             part = random.randint(min + 1, max)
#         print(f'{name} взял конфет: {part}')
#         number -= part
#         print(f'Осталось конфет - {number}')
#     else:
#         part = number % 29
#         print(f'{name} взял конфет: {part}')
#         number -= part
#         print(f'Осталось конфет - {number}')
#     return number


# min = 0
# max = 28
# candy = random.randint(29, 200)
# name_A = 'Bot'
# print(f'Привет, я - умный {name_A}')
# name_B = input('Как тебя зовут? ')
# print(f'На столе лежит {candy} конфет')
# toss = random.randint(0, 1)
# if toss:
#     print(f'Первый ход за игроком - {name_A}')
# else:
#     print(f'Первый ход за игроком - {name_B}')
# winner = play(candy, min, max, toss, name_A, name_B)

# print(f'{winner} - победитель!') 



# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом




# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

path = 'HOMEWORKS/input_data.txt'
with open (path, 'r') as data:
    input_data = data.read()

# Решение через строку

def compression(data: str):
    result = ''
    count = 1
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result += str(count) + data[i]
            count = 1
    result += str(count) + input_data[len(data) - 1]
    return result

def expansion(data: str):
    result = ''
    count = ''
    for i in range(len(data)):
        if data[i].isdigit() == True:
            count += data[i]
        else:
            count = int(count)
            result += data[i] * count
            count = ''
    return result


output_data = compression(input_data)
print(output_data)
print(expansion(output_data))


# Решение через список

# compression = []
# count = 1
# for i in range(len(input_data)-1):
#     if input_data[i] == input_data[i+1]:
#         count += 1
#     else:
#         compression.append((count, input_data[i]))
#         count = 1
# compression.append((count, input_data[len(input_data)-1]))

# print(compression)




