from typing import List
from os import path

class Service:

    def getReportName(self) -> str:
        return self.fileName

    def init(self, fileName: str):
        index = 1
        while path.exists(fileName):
            fileName = fileName.replace('.csv', '')
            fileName = fileName + '-{}.csv'.format(index)
            index += 1

        self.fileName = fileName

    def acceptGameData(self, iteration: int, gameData: List):
        pass

    def close(self):
        pass
