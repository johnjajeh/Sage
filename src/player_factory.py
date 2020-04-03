from players.always_bet import PlayerAlwaysBet
from players.difference_plus import PlayerDifferencePlus
from players.difference import PlayerDifference
from players.hard_splits import PlayerHardSplits
from players.spread import PlayerSpread
from players.player import Player

class PlayerFactory:
    def getPlayer1(self) -> Player:
        return self.player1

    def getPlayer2(self) -> Player:
        return self.player2

    def determinePlayers(self):
        self.printIntroduction()

        self.player1 = self.queryPlayer(1)
        self.player2 = self.queryPlayer(2)

    def queryPlayer(self, playerNum: int):
        switcher = {
            '1': lambda: PlayerAlwaysBet(),
            '2': lambda: PlayerDifference(),
            '3': lambda: PlayerDifferencePlus(),
            '4': lambda: PlayerHardSplits(),
            '5': lambda: PlayerSpread(),
        }

        selection = input('Select Player #{}: '.format(playerNum))

        return switcher.get(selection, lambda: PlayerAlwaysBet())

    def printIntroduction(self):
        print('-------------------------------')
        print('--        Pick Players       --')
        print('-- Input a number from below --')
        print('-------------------------------')
        print('')
        print(' [1] Always bet')
        print(' [2] Difference')
        print(' [3] Difference plus 1')
        print(' [4] Hard splits')
        print(' [5] Spread')
        print('')
