from sys import exit
from pathlib import Path
from typing import List
from services.log_service import LogService
from services.summary_service import SummaryService

DEST_DIR = '../reports/'

class Reporter:

    def __init__(self):
        self.iteration = 0
        self.data = []
        self.services = [ LogService(), SummaryService() ]

        Path(DEST_DIR).mkdir(parents=True, exist_ok=True)

    def initServices(self):
        fileName = input('Input desired file name (without extension): ')

        self.__validate(fileName)

        fileName = DEST_DIR + fileName

        for service in self.services:
            service.init(fileName)

    def recordData(self, p1Score: int, p2Score: int):
        self.data.append(p1Score)
        self.data.append(p2Score)

    def updateIteration(self, iteration: int):
        self.iteration = iteration
        
        for service in self.services:
            service.acceptGameData(self.iteration, self.data)

        self.data.clear()

    def close(self, finalData: List):
        for service in self.services:
            service.close(finalData)

            print('Report saved to {}'.format(service.getReportName()))

    def __validate(self, fileName: str):
        if '/' in fileName:
            exit('/ is not allowed in file names.')

        sections = fileName.split('.')

        if len(sections) != 1:
            exit('Invalid file name.')
