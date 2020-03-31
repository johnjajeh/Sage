from player import Player
from dealer import deal

class Sage:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def run(self): #Probably pass something in to record data for each round
        for roundNum in range(10):
            self.playRound(self.player1)
            self.playRound(self.player2)

        return (self.player1.score, self.player2.score)

    def playRound(self, player: Player):
        cards, card3 = deal()
        
        bet = 1 + player.play(cards[0], cards[1])

        if (cards[0] < card3 and card3 < cards[1]):
            player.changeScore(bet)
        else:
            player.changeScore(-bet)

    
