import requests
from twilio.rest import Client
from datetime import datetime, timedelta

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

COMPANY_NAME = "Tesla Inc"
ALPHAKEY = ""
ALPHAAPI = "https://www.alphavantage.co/query"  # https://www.alphavantage.co/query"
TIKR = "TSLA"
PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": TIKR,
    "apikey": ALPHAKEY
}

request = requests.get(ALPHAAPI, PARAMS)
print(request.json())

stock_data_daily = request.json()['Time Series (Daily)']
stock_list = [value for (key, value) in stock_data_daily.items()]

yesterday_data = stock_list[0]
day_before_data = stock_list[1]
yesterday_closing_price = yesterday_data["4. close"]
day_before_closing_price = day_before_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="",
            to=""
        )
