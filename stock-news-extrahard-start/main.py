from stock import Stock
from news import GetNews
from sms import SMS

stock = Stock()
news = GetNews(stock)
sms = SMS(news)

if news.did_change_by_5_percent():
    sms.send_message()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
