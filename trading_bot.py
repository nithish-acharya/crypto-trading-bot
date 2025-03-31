from tkinter import *
import pandas as pd
import numpy as np
import time
import requests
from pycoingecko import CoinGeckoAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Fetch Historical Crypto Data
def fetch_historical_data(crypto, currency='usd', days=365):
    cg = CoinGeckoAPI()
    try:
        data = cg.get_coin_market_chart_by_id(id=crypto, vs_currency=currency, days=days)
        prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
        return prices
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame(columns=['timestamp', 'price'])

# Calculate RSI
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=period).mean()
    avg_loss = pd.Series(loss).rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return pd.Series(rsi, name='RSI')

# Sentiment Analysis (Replace with News API)
def fetch_sentiment(crypto):
    try:
        headlines = [f"{crypto} is trending positive!", f"Concerns over {crypto} market impact."]
        analyzer = SentimentIntensityAnalyzer()
        sentiments = [analyzer.polarity_scores(headline)['compound'] for headline in headlines]
        return np.mean(sentiments) if sentiments else 0
    except Exception as e:
        print(f"Error fetching sentiment: {e}")
        return 0


# Trading Bot Logic with Improved Conditions
def trading_bot(crypto, currency='usd', rsi_period=14, buy_threshold=25, sell_threshold=65, sentiment_threshold=0):
    data = fetch_historical_data(crypto, currency)
    if data.empty:
        print("No data fetched.")
        return
    data['RSI'] = calculate_rsi(data['price'], rsi_period)

    print(f"Fetching sentiment for {crypto}...")
    sentiment_score = fetch_sentiment(crypto)

    holding = False  # Track whether the bot is holding the asset
    for i in range(len(data)):
        price = data['price'][i]
        rsi = data['RSI'][i]
        date = data['timestamp'][i]

        if rsi < buy_threshold and sentiment_score > sentiment_threshold and not holding:
            action=(f"Buy {crypto} at ${price:.2f} on {date} (RSI: {rsi:.2f}, Sentiment: {sentiment_score:.2f})")
            holding = True  # Assume the bot buys the asset

        elif rsi > sell_threshold and sentiment_score < -sentiment_threshold and holding:
            action=(f"Sell {crypto} at ${price:.2f} on {date} (RSI: {rsi:.2f}, Sentiment: {sentiment_score:.2f})")
            holding = False  # Assume the bot sells the asset
    txt= Label(vp, text=action, fg="white", bg="#002240", font="Magneto 35 bold").place(relx=0.1, rely=0.8)
    if sentiment_score > 0.3:
        statement=("Positive sentiment detected.")
        txt= Label(vp, text=statement, fg="green", bg="#002240", font="Magneto 35 bold").place(relx=0.1, rely=0.9)
        ss=(f"Sentiment score: {sentiment_score}")
        txt= Label(vp, text=ss, fg="green", bg="#002240", font="Magneto 35 bold").place(relx=0.3, rely=0.7)
    
    elif sentiment_score < -0.3:
        statement=("Negative sentiment detected.")
        txt= Label(vp, text=statement, fg="red", bg="#002240", font="Magneto 35 bold").place(relx=0.1, rely=0.9)
        ss=(f"Sentiment score: {sentiment_score}")
        txt= Label(vp, text=ss, fg="red", bg="#002240", font="Magneto 35 bold").place(relx=0.3, rely=0.7)
    else:
        statement=("Neutral sentiment detected.")
        txt= Label(vp, text=statement, fg="white", bg="#002240", font="Magneto 35 bold").place(relx=0.1, rely=0.9)
        ss=(f"Sentiment score: {sentiment_score}")
        txt= Label(vp, text=ss, fg="white", bg="#002240", font="Magneto 35 bold").place(relx=0.3, rely=0.7)
    






def HOME():
    global vp
    def on_submit():
        # Fetch the value from the Entry widget
        crypto_name = e2.get().strip()
        if crypto_name:
            trading_bot(crypto_name)  # Pass the input to trading_bot
        else:
            print("Please enter a cryptocurrency name.")

    vp = Tk()
    vp.geometry("1000x1000")
    vp.title("HOME Page")
    vp.configure(bg="#002240")
    
    t2 = Label(vp, text="HOME PAGE", fg="orange", bg="#002240", font="Magneto 35 bold")
    t2.place(relx=0.3, rely=0.2)
    
    t3 = Label(vp, text="Crypto Name", fg="orange", bg="#002240", font="Magneto 35 bold")
    t3.place(relx=0.1, rely=0.4)
    
    e2 = Entry(vp, fg="orange", bg="white", font="Courier 25 bold")
    e2.place(relx=0.5, rely=0.4)
    
    b2 = Button(vp, text="SUBMIT", fg="orange", bg="#002240", activeforeground="green", font="Courier 25 bold", command=on_submit)
    b2.place(relx=0.5, rely=0.6)

    vp.mainloop()

HOME()

