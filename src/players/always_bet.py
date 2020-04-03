from players.player import Player

class PlayerAlwaysBet(Player):
    def play(self, low: int, high: int) -> int:
        return 9;
