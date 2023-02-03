
board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

win_com = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))


def draw_board():
    print('-------------')
    for i in range(3):
        for y in range(3):
            print('|', board[y + i * 3], end = ' ')
        print(f'|\n-------------')


def get_board():
    global board
    return board


def set_board(position: str, mark: str):
    global board
    board[int(position) - 1] = mark























