from players.player import Player

class PlayerDifferencePlus(Player):
    def play(self, low: int, high: int) -> int:
        return high - low + 1;
