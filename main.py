import ccxt
import os
from dotenv import load_dotenv
import time

# Załaduj klucze API
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
secret = os.getenv("BINANCE_SECRET")
symbol = os.getenv("SYMBOL", "BTC/USDT")
buy_thresh = float(os.getenv("BUY_THRESHOLD", "-1.0"))
sell_thresh = float(os.getenv("SELL_THRESHOLD", "1.0"))

exchange = ccxt.binance({
    "apiKey": api_key,
    "secret": secret,
    "options": {"defaultType": "spot"},
})

def get_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker["last"]

def simple_strategy(current_price, last_price):
    change_pct = ((current_price - last_price) / last_price) * 100
    if change_pct <= buy_thresh:
        return "BUY"
    if change_pct >= sell_thresh:
        return "SELL"
    return "HOLD"

def main():
    last_price = get_price()
    print(f"Start price: {last_price:.2f}")

    while True:
        try:
            price = get_price()
            signal = simple_strategy(price, last_price)
            print(f"Price: {price:.2f} → Signal: {signal}")

            if signal == "BUY":
                print(f"  🟢 Kupujemy {symbol} @ {price:.2f}")
                # Tu moglibyśmy wywołać order create
            if signal == "SELL":
                print(f"  🔴 Sprzedajemy {symbol} @ {price:.2f}")
                # Tu moglibyśmy wywołać order create

            last_price = price
            time.sleep(10)

        except Exception as e:
            print("Błąd:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
