import commands

def start():
    commands.set_player()
    if commands.toss():
        commands.switch()
    while commands.get_total() > 0:
        commands.game_turn()
    print(f'{commands.get_current_player()} победил!')




