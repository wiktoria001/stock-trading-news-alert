import requests

class Stock:
    def __init__(self):
        self.STOCK = "TSLA"
        self.COMPANY_NAME = "Tesla Inc"
        self.ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"
        self.parameters = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": self.STOCK,
            "apikey": "0AL630623E93J3GO"
        }
        self.yesterday_close = 0
        self.before_yesterday_close = 0

    def get_response(self):
        alphavantage_response = requests.get(url=self.ALPHAVANTAGE_URL, params=self.parameters)
        alphavantage_response.raise_for_status()
        alphavantage_data = alphavantage_response.json()
        two_last_days = list(alphavantage_data["Time Series (Daily)"])[:2]  # <--- this is a List

        self.yesterday_close = float(alphavantage_data["Time Series (Daily)"][two_last_days[0]]["4. close"])
        self.before_yesterday_close = float(alphavantage_data["Time Series (Daily)"][two_last_days[1]]["4. close"])
