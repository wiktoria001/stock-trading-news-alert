import html
from twilio.rest import Client
from news import GetNews


class SMS:
    def __init__(self, news: GetNews):
        self.news = news
        self.account_sid = "AC5db882706cce480fa2ce7cfdf5f66c4a"
        self.auth_token = "faed9779459ea6c0b9b1adc998413d19"
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        index = 0
        for _ in self.news.articles:
            headline = html.unescape(self.news.articles[index]['title'])
            brief = html.unescape(self.news.articles[index]['content'])
            message = self.client.messages \
                .create(
                body="TSLA: percentages\n"
                     f"Headline: \n{headline}\n"
                     f"Brief: \n{brief}",
                from_="+17262273730",
                to="+48511970389"
            )
            index += 1
            print(message.status)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
