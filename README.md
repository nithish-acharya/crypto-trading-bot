📈 Cryptocurrency Trading Bot with RSI & Sentiment Analysis
This project is a Python-based cryptocurrency trading bot that utilizes Relative Strength Index (RSI) and sentiment analysis to generate buy/sell signals. It features a Tkinter-based GUI for user interaction and fetches live crypto data from CoinGecko API.

⚡ Features
✅ Fetch Historical Data – Retrieves past price data from CoinGecko.
✅ RSI Calculation – Computes the 14-day RSI to determine overbought/oversold conditions.
✅ Sentiment Analysis – Uses VADER Sentiment Analysis to analyze crypto market trends.
✅ Automated Trading Signals – Generates buy/sell recommendations based on RSI & sentiment score.
✅ Tkinter GUI – Provides an interactive interface for users to enter a cryptocurrency name and receive insights.

🛠 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/crypto-trading-bot.git
cd crypto-trading-bot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Make sure Python is installed on your system.

🚀 Usage
Run the bot

bash
Copy
Edit
python trading_bot.py
Enter the cryptocurrency name (e.g., bitcoin, ethereum) in the GUI.

The bot fetches market data, calculates RSI, and analyzes sentiment.

Trading decisions (Buy/Sell/Neutral) are displayed in the GUI based on RSI & sentiment thresholds.

📊 Trading Strategy
BUY: When RSI is below 25 and sentiment score is positive.

SELL: When RSI is above 65 and sentiment score is negative.

HOLD: When the market is neutral.

🔧 Technologies Used
Python 🐍

Tkinter (GUI)

CoinGecko API (Crypto price data)

VADER Sentiment Analysis (Market sentiment detection)

Pandas & NumPy (Data processing)

📜 License
This project is open-source and available under the MIT License.

