
import board
import game

game.set_players()
if game.toss():
    game.switch_player()
print(f"Первым ходит '{game.get_mark()}' под управлением {game.get_current_player()}")
while True:
    if game.game_turn():
        break





















