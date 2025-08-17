from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol: str, side: str, quantity: float):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        return order
    except BinanceAPIException as e:
        raise Exception(f"Market order failed: {str(e)}")
