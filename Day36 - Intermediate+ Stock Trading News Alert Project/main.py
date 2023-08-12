import requests
from dotenv import load_dotenv
from datetime import datetime
from newsapi import NewsApiClient
import os
import random
from twilio.rest import Client


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("ALPHA_ADVANTAGE_API_KEY")
NEWS_API = os.environ.get("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_status():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response = response.json()["Time Series (Daily)"]
    return response

def get_dates():
    current_date = str(datetime.now().date()).split("-")
    recent_day = int(current_date[-1]) - 2
    yesterday = recent_day - 1

    year_month = f"{current_date[0]}-{current_date[1]}"
    dates = [f"{year_month}-{recent_day}", f"{year_month}-{yesterday}"]
    return dates
def get_stock_percentage(recent, yesterday):
    amounts = [recent, yesterday]
    larger_amount = max(amounts)
    smaller_amount = min(amounts)
    difference = larger_amount - smaller_amount
    percentage = (difference / 100) * larger_amount

    return percentage
print("getting latest stocks exchanges data...")
recent_date = get_dates()[0]
yesterday_date = get_dates()[1]
stock_data = [{key:value}for (key, value) in get_stock_status().items() if key == recent_date or key == yesterday_date]
print("calculating difference in stocks market...")
recent_date_close_amount = float(stock_data[0][recent_date]["4. close"])
yesterday_date_close_amount = float(stock_data[1][yesterday_date]["4. close"])
recent_stock_percentage = get_stock_percentage(recent=recent_date_close_amount, yesterday=yesterday_date_close_amount)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
newsapi = NewsApiClient(api_key=NEWS_API)
def get_news():
    print("fetching relevant news...")
    all_news = newsapi.get_everything(q='tesla')
    articles = all_news["articles"]
    big_news = random.choice(articles)

    return big_news

if recent_stock_percentage >= 5:
    news = get_news()
    title = news["title"]
    description = news["description"]
    content = news["content"]
    arrow_indicator = "🔺"
    if yesterday_date_close_amount > recent_date_close_amount:
        arrow_indicator = "🔻"
    body_message = f"TSLA --> {arrow_indicator}{round(recent_stock_percentage)}\n{title}\n{description}\n{content}"
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    print("sending sms for the user...")
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+13344909407',
    body=body_message,
    to='+639619551081'
    )

    print("new message arrived check your phone now")
    print(body_message)
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

