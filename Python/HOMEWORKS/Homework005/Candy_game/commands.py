import random

total = 100
player_one = ''
player_two = ''
current_player = player_one
bot_mode = False


def set_max_total():
    global total
    while True:
        try:
            total = int(input('Введите общее количество конфет: '))
            break   
        except ValueError:
            print('Введите цифрами')


def get_total():
    global total
    return total


def set_total(take: int):
    global total
    total -= take


def get_current_player():
    global current_player
    return current_player


def switch():
    global current_player
    global player_one
    global player_two
    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one


def set_player():
    global player_one
    global player_two
    global bot_mode
    global current_player
    while player_one == '':
        player_one = input('Первый игрок, представьтесь: ')
        current_player = player_one
    player_two = input('Второй игрок, представьтесь, или '
                            f'нажмите Enter для игры против бота: ')
    if not player_two:
        player_two = 'Бот'
        bot_mode = True
    set_max_total()

    
def toss():
    return random.randint(0, 1)


def game_turn():
    global total
    global current_player
    switch()
    if current_player == player_two and bot_mode:
        take = bot_turn()
    else:
        take = player_turn()
    set_total(take)
    print(f'{current_player} взял {take} конфет. '
          f'На столе осталось {total}')
        

def bot_turn():
    global total
    take = 0
    if total <= 28:
        take = total
    else:
        take = total % 29
        if take == 0:
            take = random.randint(1, 28)
    return take


def player_turn():
    take = 0
    while True:
        try:
            take = int(input(f'{current_player}, '
                             f'возьмите конфеты: '))
            if 0 < take < 29:
                break 
            elif take > 28:
                print(f'{current_player}, нельзя взять больше 28 конфет')
            elif take == 0:
                print(f'{current_player}, нельзя пропускать ход')
            else:
                print(f'{current_player}, нельзя взять отрицательное число конфет')
        except ValueError:
            print('Введите цифрами')
    return take

    
    










