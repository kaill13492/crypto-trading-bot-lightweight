# crypto-trading-bot-lightweight
Minimal crypto trading bot with modular strategies (Binance, Bybit, OKX, …)
# Crypto Trading Bot (Lightweight)

A clean, modular, easy-to-extend trading bot for centralized crypto exchanges.

**Currently supported exchanges** (via ccxt):  
Binance, Bybit, OKX, KuCoin, Gate.io, MEXC, Bitget

**Built-in strategy templates:**
- Grid trading (spot & futures)
- DCA / cost averaging
- RSI + momentum
- Breakout
- Funding-rate arbitrage helper
- Simple mean reversion

## Quick Start

```bash
git clone https://github.com/yourusername/crypto-trading-bot-lightweight.git
cd crypto-trading-bot-lightweight
python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate       # Windows
pip install -r requirements.txt├── config/             # yaml strategy & exchange configs
├── strategies/         # each strategy in separate file
├── core/
│   ├── exchange.py
│   ├── order_manager.py
│   └── risk.py
├── notifications/      # telegram, discord, email...
├── utils/
├── backtest/           # very basic pandas/vectorbt backtesting
├── .env.example
├── main.py
└── requirements.txt
cp .env.example .env
# ← edit .env with your API keys!
python main.py --strategy grid --symbol BTC/USDT



# 🚀 WITAJ PRZYBYSZU

Jeśli to czytasz, to znaczy że:

✅ repo się otworzyło  
✅ Git nie wybuchł  
✅ a to oznacza tylko jedno…

## 💎 BARDZO ŁADNE REPO 💎

⭐ 10/10  
⭐ poleciłbym koledze  
⭐ działa nawet u mnie  

> Autor repo: człowiek kultury  
> Repo: piękniejsze niż dokumentacja  

Miłego scrollowania 😎
