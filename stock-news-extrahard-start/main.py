import requests
import datetime
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHAVANTAGE_URL = 'https://www.alphavantage.co/query'
parameters_alphavantage = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "0AL630623E93J3GO"
}
alphavantage_response = requests.get(url=ALPHAVANTAGE_URL, params=parameters_alphavantage)
alphavantage_data = alphavantage_response.json()

two_last_days = list(alphavantage_data["Time Series (Daily)"])[:2]  # <--- this is a List

yesterday_close = float(alphavantage_data["Time Series (Daily)"][two_last_days[0]]["4. close"])
before_yesterday_close = float(alphavantage_data["Time Series (Daily)"][two_last_days[1]]["4. close"])


def did_change_by_5_percent(day1, day2):
    five_percent = (5/100) * day2
    if (day2 - five_percent) >= day1 or day1 >= (day2 + five_percent):
        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        now = datetime.datetime.now()
        date = now.date()

        NEWS_URL = "https://newsapi.org/v2/everything"
        news_parameters = {
            "q": COMPANY_NAME,
            "from": date,
            "sortBy": "popularity",
            "language": "en",
            "apiKey": "e603fc1e4f844b0b8aa136b6a5c1363a"
        }
        news_reponse = requests.get(url=NEWS_URL, params=news_parameters)
        news_data = news_reponse.json()

        #  Get 3 last articles in a list
        articles = list(news_data["articles"])[:3]

        index = 0
        for article in articles:
            headline = html.unescape(articles[index]['title'])
            print(headline)
            content = html.unescape(articles[index]['content'])
            print(content)
            print(".")
            index += 1


# did_change_by_5_percent(day1=yesterday_close, day2=before_yesterday_close)
did_change_by_5_percent(day1=160, day2=before_yesterday_close)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

