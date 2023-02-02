import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
function = "TIME_SERIES_DAILY_ADJUSTED"
apikey = "037REWG6RPOXG0GL"
news_key = "71c23c97ec0a4bbb8bd3b6066a1c23e9"
today = str(date.today() - timedelta(days=2))
print(today)

stock_parameters = {
    "function": function,
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": apikey,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = 'https://www.alphavantage.co/query'

r = requests.get(url, params=stock_parameters)
data = r.json()

yesterday_data = data["Time Series (Daily)"][today]
print(yesterday_data)
close = float(yesterday_data["4. close"])
open = float(yesterday_data["1. open"])
change_rate = (open - close)/open
print(change_rate)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    "q":COMPANY_NAME,
    "from":today,
    "language":"en",
    "pageSize":10,
    "sortBy":"popularity&",
    "apiKey":news_key,
}
url = ('https://newsapi.org/v2/everything?')

if change_rate > 0.05 or change_rate < -0.05:
    print("get news")
    response = requests.get(url, params=news_parameters)
    print(response.json())

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

