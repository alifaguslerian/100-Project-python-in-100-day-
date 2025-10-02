import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # biar nggak 401
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_html(html):
    return BeautifulSoup(html, "html.parser")

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {
        "data-symbol": ticker,
        "data-field": "regularMarketPrice"
    })
    if price_tag:
        # Bersihin angka (buang koma)
        return price_tag.text.replace(",", "")
    else:
        print("Could not find the stock price on the page.")
        return None

def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: ${price}")
        time.sleep(interval)

def main():
    print("Welcome to the Stock Price Tracker!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").strip().upper()
    interval = int(input("Enter the interval in seconds to check the price (default is 60): ") or 60)
    print(f"Tracking {ticker} stock price every {interval} seconds...")
    track_stock_price(ticker, interval)

if __name__ == "__main__":
    main()
