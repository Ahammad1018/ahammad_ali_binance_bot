# ahammad_ali_binance_bot

# Binance Futures Trading Bot (Testnet)

CLI-based Python bot for Binance **USDT-M Futures**  
✅ Market & Limit Orders  
✅ Bonus: Stop-Limit Orders  
✅ Input validation + logging  
✅ Ready for submission (ZIP or private GitHub repo)

---

## 🔧 Setup

```bash
pip install python-binance

1️⃣ Market Order
python src/cli.py --api_key=YOUR_KEY --api_secret=YOUR_SECRET --symbol=BTCUSDT --side=BUY --type=MARKET --quantity=0.001

2️⃣ Limit Order
python src/cli.py --api_key=YOUR_KEY --api_secret=YOUR_SECRET --symbol=BTCUSDT --side=SELL --type=LIMIT --quantity=0.001 --price=63000

3️⃣ Stop-Limit Order (Advanced)
python src/cli.py --api_key=YOUR_KEY --api_secret=YOUR_SECRET --symbol=BTCUSDT --side=BUY --type=STOP_LIMIT --quantity=0.001 --stop_price=62000 --price=62300
