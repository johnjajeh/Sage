from services.service import Service
from typing import List
import csv

class SummaryService(Service):
    def init(self, fileName: str):
        super().init(fileName + '-summary.csv')

        self.roundTotals = [0 for i in range(20)]

    def acceptGameData(self, iteration: int, gameData: List):
        for k, v in enumerate(gameData):
            self.roundTotals[k] += v;

    def close(self, finalData: List):
        iterations, p1Name, p2Name = finalData
        avgData = []

        for total in self.roundTotals:
            avgData.append(total / iterations)

        file = open(self.getReportName(), 'w', newline='')
        writer = csv.writer(file)

        writer.writerow(['p1Name', 'p2Name'] + ['p1AvgScore', 'p2AvgScore'] * 10)
        writer.writerow([p1Name, p2Name] + avgData)

        file.close()
