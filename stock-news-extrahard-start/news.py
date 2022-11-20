import datetime
import requests
from stock import Stock


class GetNews:
    def __init__(self, stock: Stock):
        self.now = datetime.datetime.now()
        self.date = self.now.date()
        self.stock = stock
        self.NEWS_URL = "https://newsapi.org/v2/everything"
        self.day1 = 100
        self.day2 = self.stock.before_yesterday_close
        self.articles = []

    def did_change_by_5_percent(self):
        five_percent = (5 / 100) * self.day2
        if (self.day2 - five_percent) >= self.day1 or self.day1 >= (self.day2 + five_percent):
            news_parameters = {
                "q": self.stock.COMPANY_NAME,
                "from": self.date,
                "sortBy": "popularity",
                "language": "en",
                "apiKey": "e603fc1e4f844b0b8aa136b6a5c1363a"
            }
            news_reponse = requests.get(url=self.NEWS_URL, params=news_parameters)
            news_reponse.raise_for_status()
            news_data = news_reponse.json()

            self.articles = list(news_data["articles"])[:3]
            return True
        else:
            return False



