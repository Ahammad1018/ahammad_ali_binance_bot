from binance.exceptions import BinanceAPIException

def place_limit_order(client, symbol: str, side: str, quantity: float, price: float, time_in_force="GTC"):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce=time_in_force
        )
        return order
    except BinanceAPIException as e:
        raise Exception(f"Limit order failed: {str(e)}")
