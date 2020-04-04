from players.player import Player
from dealer import deal
from reporter import Reporter

class Sage:
    def __init__(self, player1: Player, player2: Player, reporter: Reporter):
        self.player1 = player1
        self.player2 = player2
        self.reporter = reporter

    def run(self): #Probably pass something in to record data for each round
        for roundNum in range(10):
            self.__playRound(self.player1)
            self.__playRound(self.player2)

            self.reporter.recordData(self.player1.score, self.player2.score)

        return (self.player1.score, self.player2.score)

    def __playRound(self, player: Player):
        cards, card3 = deal()

        bet = 1 + player.play(cards[0], cards[1])

        if (cards[0] < card3 and card3 < cards[1]):
            player.changeScore(bet)
        else:
            player.changeScore(-bet)
