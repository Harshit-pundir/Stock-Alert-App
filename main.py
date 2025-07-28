import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------ CONFIG ------------------ #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENT_THRESHOLD = 1  # Set threshold % to trigger news/SMS

# API Keys and Credentials from environment
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")

# ------------------ FUNCTION DEFINITIONS ------------------ #
def get_stock_data(symbol):
    """Fetch daily stock data from Alpha Vantage API"""
    stock_endpoint = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY,
    }
    response = requests.get(stock_endpoint, params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    return list(data.values())

def calculate_difference(data_list):
    """Calculate % difference between two latest closing prices"""
    yesterday_close = float(data_list[0]["4. close"])
    day_before_close = float(data_list[1]["4. close"])
    diff = abs(yesterday_close - day_before_close)
    diff_percent = (diff / day_before_close) * 100
    trend = "🔺" if yesterday_close > day_before_close else "🔻"
    return diff_percent, trend

def get_news(query):
    """Fetch top 3 news articles related to the company"""
    news_endpoint = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": query,
        "language": "en",
        "sortBy": "publishedAt"
    }
    response = requests.get(news_endpoint, params=params)
    response.raise_for_status()
    return response.json()["articles"][:3]

def format_articles(articles, symbol, trend, percent):
    """Format messages for SMS"""
    return [
        f"{symbol}: {trend}{round(percent, 2)}%\n"
        f"📰 Headline: {article['title']}\n"
        f"📄 Brief: {article['description'] or 'No description available.'}"
        for article in articles
    ]

def send_sms(messages):
    """Send messages using Twilio"""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for msg in messages:
        message = client.messages.create(
            body=msg,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER,
        )
        print(f"✅ Message sent: {message.status}")

# ------------------ MAIN PROGRAM ------------------ #
if __name__ == "__main__":
    try:
        stock_data = get_stock_data(STOCK)
        diff_percent, trend_symbol = calculate_difference(stock_data)

        print(f"[INFO] Price Change: {round(diff_percent, 2)}% {trend_symbol}")

        if diff_percent > PERCENT_THRESHOLD:
            print("[INFO] Significant change detected. Fetching news...")
            news_articles = get_news(COMPANY_NAME)
            message_list = format_articles(news_articles, STOCK, trend_symbol, diff_percent)
            send_sms(message_list)
        else:
            print("[INFO] No major change. No SMS sent.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")