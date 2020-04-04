from services.service import Service
from typing import List
import csv

class LogService(Service):

    def init(self, fileName: str):
        super().init(fileName + '-log.csv')

        file = open(self.getReportName(), 'w', newline='')
        writer = csv.writer(file)

        writer.writerow(['iteration'] + ['p1score', 'p2score'] * 10)

        self.file = file
        self.writer = writer

    def acceptGameData(self, iteration: int, gameData: List):
        self.writer.writerow([iteration] + gameData)

    def close(self, finalData: List):
        self.file.close()
