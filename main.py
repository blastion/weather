import requests


class getWeather:
    def __init__(self, city:str) -> None:
        self.city = city
        self.api_key = ''

    def weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': self.api_key, 'q': self.city, 'units': 'metric'}
        response = requests.get(url, params=params)
        data = response.json()
        temp = data['main']['temp']
        return temp

print(getWeather('São Paulo').weather())
