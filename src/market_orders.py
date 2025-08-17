from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol: str, side: str, quantity: float, dry_run: bool = False):
    """
    Place a futures market order. If dry_run=True, return the order payload
    without calling the Binance API.
    """
    payload = {
        "symbol": symbol,
        "side": side.upper(),
        "type": "MARKET",
        "quantity": quantity
    }

    if dry_run:
        return {"DRY_RUN": True, "payload": payload}

    try:
        return client.futures_create_order(**payload)
    except BinanceAPIException as e:
        raise Exception(f"Market order failed: {str(e)}")
