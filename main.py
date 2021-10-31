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

class WebHook:
    def __init__(self, url:str, temp:float) -> None:
        self.url = url
        self.temp = temp

    def send(self):
        data = {"value1": str(self.temp)}
        print(data)
        requests.post(self.url, json=data)

sao_paulo = getWeather('São Paulo')
tweet = WebHook('https://maker.ifttt.com/trigger/t/with/key/beAZ5WtBpub2VZ6TM24TWW', sao_paulo.weather())
tweet.send()
