class Player:
    def __init__(self):
        self.score = 100

    def getName(self):
        return self.__class__.__name__

    def changeScore(self, change: int):
        self.score += change

    def play(self, low: int, high: int) -> int: #TODO add more info if needed (maybe round and other player score)
        pass
