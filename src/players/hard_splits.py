from players.player import Player

class PlayerHardSplits(Player):
    def play(self, low: int, high: int) -> int:
        difference = high - low

        if difference < 4:
            return 0

        if difference == 4 || difference == 5:
            return 5

        return 9
