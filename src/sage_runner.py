from sage_game import Sage
from player_always_bet import PlayerAlwaysBet

player1 = PlayerAlwaysBet()
player2 = PlayerAlwaysBet()

game = Sage(player1, player2)
p1, p2 = game.run()

print("Player 1: ".format(p1))
print("Player 2: ".format(p2))
