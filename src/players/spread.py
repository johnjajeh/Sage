from players.player import Player

class PlayerSpread(Player):
    def play(self, low: int, high: int) -> int:
        if high - low >= 6:
            return 9

        return 0;
