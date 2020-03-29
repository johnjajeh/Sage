from sage_game import Sage
from player_always_bet import PlayerAlwaysBet

player1 = PlayerAlwaysBet()
player2 = PlayerAlwaysBet()

game = Sage(player1, player2)
game.startGame()
