# import random

# import board as b

# current_player = ''
# player_one_name = ''
# player_two_name = ''
# current_player = player_one_name
# mark = 'x'
# game_bot_mode = False


# def set_player_names():
#     global player_one_name
#     global player_two_name
#     global game_bot_mode
#     global current_player
#     while player_one_name == '':
#         player_one_name = input('Первый игрок, представьтесь: ')
#     current_player = player_one_name
#     player_two_name = input('Второй игрок, представьтесь (Enter для игры против боте): ')
#     if not player_two_name:
#         player_two_name = 'Ботяо'
#         game_bot_mode = True

# def switch_player():
#     global mark
#     global current_player
#     global player_one_name
#     global player_two_name
#     if mark == 'x':
#         mark = '0'
#     else:
#         mark = 'x'

# def game_turn():
#     global mark
#     global current_player
#     global player_one_name
#     global player_two_name
#     switch_player()
#     position = ''
#     if game_bot_mode and current_player == player_two_name:
#         position = bot_turn()
#     else:
#         b.draw_board()


#     if current_player == player_two_name and game_bot_mode:
#         position = bot_turn()
        
#     else:
#         position = player_turn()
#     b.draw_board()
#     b.set_board(position, mark)
#     board = b.get_board
#     for pos in b.win_con:
#         if board[pos[0]] == board[pos[1]] == board[pos[2]]:
#             print(f'Побеждает {mark} под управлением {current_player}')
#             return True
    

# def player_turn():
#     global current_player
#     while True:
#         try:
#             position = input(f'{current_player}, введите позицию: ')
#             if position in b.get_board():
#                 return position
#             else:
#                 print('Эта позиция занята')
#         except ValueError:
#             print('Введите цифру')

# def bot_turn():
#     global mark
#     board = b.get_board()
#     if '4' in board:
#         return 4
#     else:
#         for pos in [0, 2, 6, 8]:
#             if board[pos].isdigit():
#                 return pos
#         for pos in b.win_con:
#             if board[pos[0]] == board[pos[1]] == mark:
#                 return pos[2]
#             if board[pos[1]] == board[pos[2]] == mark:
#                 return pos[0]
#             if board[pos[0]] == board[pos[2]] == mark:
#                 return pos[1]
#     while True:
#         pos = str(random.randint(1, 9))
#         if pos in board:
#             return pos





import random

import board as play_board

player_one_name = ''
player_two_name = ''
current_player = ''
mark = 'X'
game_bot_mode = False

def get_current_player():
    global current_player
    return current_player

def get_mark():
    global mark
    return mark

def set_player_names():
    global player_one_name
    global player_two_name
    global game_bot_mode
    global current_player
    while player_one_name == '':
        player_one_name = input('Первый игрок представьтесь: ')
        current_player = player_one_name
    player_two_name = input('Второй игрок представьтесь или '
                            'нижмите Enter для игры против бота: ')
    if not player_two_name:
        player_two_name = 'Бот'
        game_bot_mode = True

def toss():
    return random.randint(0, 1)

def switch_player():
    global mark
    global current_player
    global player_one_name
    global player_two_name
    if mark == 'X':
        current_player = player_two_name
        mark = 'O'
    else:
        current_player = player_one_name
        mark = 'X'


def reverse_mark():
    global mark
    if mark == 'X':
        return 'O'
    else:
        return 'X'


def game_turn():
    global mark
    global current_player 
    global player_one_name
    global player_two_name
    for pos in play_board.get_board():
        if pos.isdigit():
            break
    else:
        play_board.draw_board()
        print('Ничья')
        return True
    if game_bot_mode and current_player == player_two_name:
        position = bot_turn()
    else:
        play_board.draw_board()
        position = player_turn()
    play_board.set_board(position, mark) 
    board = play_board.get_board()
    for pos in play_board.win_con:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            play_board.draw_board()
            return True
    switch_player()


def player_turn():  
    global current_player
    while True: 
        try:
            position = input(f'{current_player}, введите позицию: ')
            if position in play_board.get_board():
                return position
            elif 0 < int(position) < 9:
                print('Эта позиция занята')
            else: 
                print('Такой позиции нет')
        except:
            print('Введите позицию цифрой')


def bot_turn():
    global mark
    board = play_board.get_board()
    if '5' in board:
        return 5
    self_win = check_pre_win(board, mark)
    if self_win:
        return self_win + 1
    enemy_win = check_pre_win(board, reverse_mark())
    if enemy_win:
        return enemy_win + 1
    for pos in {'1', '3', '7', '9'}:
        if pos in board:
            return pos
    while True:
        pos = str(random.randint(1, 9))
        if pos in board:
            return pos


def check_pre_win(board: list, marker: str):
    for pos in play_board.win_con:
        if (board[pos[0]] == board[pos[1]] == marker) and board[pos[2]].isdigit():
            return pos[2]
        elif (board[pos[2]] == board[pos[1]] == marker) and board[pos[0]].isdigit():
            return pos[0]
        elif (board[pos[2]] == board[pos[0]] == marker) and board[pos[1]].isdigit():
            return pos[1]


















