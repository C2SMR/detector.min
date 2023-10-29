import time
import sys

from api import API
from alert import Alert
from city import CITY


class Main:

    def __init__(self):
        self.alert = None
        self.actual_data_predict_picture: object = None
        self.one_hour: int = 0
        self.time_for_one_hour: float = time.time()
        self.array_api: list[API] = []
        for city in CITY:
            self.array_api.append(API(city[0], sys.argv[1],
                                      city[1], city[2]))
        self.run()

    @property
    def verif_time_one_hour(self) -> bool:
        if time.time() - self.time_for_one_hour > self.one_hour:
            self.one_hour = 60 * 60
            self.time_for_one_hour = time.time()
            return True
        return False

    def run(self):
        while True:

            if self.verif_time_one_hour:
                for i in range(len(CITY)):
                    self.array_api[i].add_data_city(0, 0, 0),
                    self.alert: Alert = Alert(CITY[i][1], CITY[i][2],
                                              self.actual_data_predict_picture,
                                              self.array_api[i])
                    self.alert.run()


if __name__ == '__main__':
    Main()
