from players.player import Player

class PlayerDifference(Player):
    def play(self, low: int, high: int) -> int:
        return high - low;
