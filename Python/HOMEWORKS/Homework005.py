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



# ИГРА ЧЕЛОВЕКА С УМНЫМ БОТОМ

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

# ИГРА В 'КРЕСТИКИ - НОЛИКИ'

# number = list(range(1, 10))
# win_number = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# def game_board():
#     print('-------------')
#     for i in range(3):
#         for y in range(3):
#             print('|', number[y + i * 3], end = ' ')
#         print(f'|\n-------------')

# def player_turn(player: str):
#     while True:
#         try:
#             turn = int(input(f'Куда поставить {player}: '))
#             if 0 < turn < 10:
#                 if str(number[turn - 1]) not in 'XO':
#                     number[turn - 1] = player
#                     return number
#                 else:
#                     print('Эта клетка уже занята!')
#             else: 
#                 print('Введите цифру с игрового поля')
#         except:
#             print('Введите цифру с игрового поля')

# def win_check():
#     for each in win_number:
#         if number[each[0] - 1] == number[each[1] - 1] == number[each[2] - 1]:
#             return number[each[1] - 1]
#     else:
#         return False


# def play():
#     count = 0
#     while True:
#         game_board()
#         if count % 2 == 0:
#             player_turn('X')
#         else:
#             player_turn('O')
#         if count > 3:
#             winner = win_check()
#             if winner:
#                 game_board()
#                 print(f'{winner} победил!')
#                 break
#         count += 1
#         if count == 9:
#             game_board()
#             print('Ничья')
#             break
    

# play()


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def compression(path_in: str, path_out: str):
    with open (path_in, 'r') as data:
        data = data.read()
    result = ''
    count = 1
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result += str(count) + data[i]
            count = 1
    result += str(count) + data[len(data) - 1]
    with open (path_out, 'w') as data:
        data.write(result)
    return result

def expansion(path_in: str, path_out: str):
    with open (path_in, 'r') as data:
        data = data.read()
    result = ''
    count = ''
    for i in range(len(data)):
        if data[i].isdigit() == True:
            count += data[i]
        else:
            count = int(count)
            result += data[i] * count
            count = ''
    with open (path_out, 'w') as data:
        data.write(result)
    return result

def main():
    path_in = 'HOMEWORKS/input_data.txt'
    path_out = 'HOMEWORKS/output_data.txt'
    
    compression_data = compression(path_in, path_out)
    print(compression_data)
    
    expansion_data = expansion(path_out, path_in)
    print(expansion_data)

main()   





