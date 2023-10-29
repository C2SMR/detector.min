from api import API
from weather import Weather


class Alert:
    def __init__(self, latitude: float, longitude: float,
                 data_picture: object, api: API):
        self.number_alerts = None
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.data_picture: object = data_picture
        self.api: API = api
        self.weather: Weather = Weather(self.latitude, self.longitude)
        self.api.delete_alert_by_city()  # delete old alert picture
        self.run()

    def run(self) -> None:
        self.number_alerts = 0
        self.rain()
        self.hard_wind()
        self.hot()
        self.change_flag()

    def rain(self) -> None:
        if self.weather.get_precipitation() > .8:
            self.number_alerts += 1
            self.api.add_alert(1, "Pluie")

    def hard_wind(self) -> None:
        if self.weather.get_wind_speed() > 60:
            self.number_alerts += 1
            self.api.add_alert(2, "Vent violents")

    def hot(self) -> None:
        if self.weather.get_temperature() > 35:
            self.number_alerts += 1
            self.api.add_alert(0, "Température très élevés")

    def change_flag(self):
        if self.number_alerts < 2:
            self.api.set_flag(0)
        elif self.number_alerts < 5:
            self.api.set_flag(1)
        else:
            self.api.set_flag(2)
