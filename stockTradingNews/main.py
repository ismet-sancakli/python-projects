import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Your API Key"
NEWS_API_KEY = "Your API Key"
TWILIO_SID = "Your API Key"
TWILIO_AUTH_TOKEN = "Your API Key"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
#  Get yesterday's closing stock price
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()] # It will return only value without key.
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "↑"
else:
    up_down = "↓"


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = (difference / float(yesterday_closing_price)) * 100
# print(diff_percent)

# If percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Use Python slice() operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)

    # Create a new list of the first 3 article's headline and description using list comprehension.
    "Headlines: {article title} \nBrief: {article description}" # This is an outline.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadlines: {article['title']} \nBrief: {article['description']}" for article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        client.messages.create(
            body=article,
            from_="your twilio number",
            to="your phone number"
        )

