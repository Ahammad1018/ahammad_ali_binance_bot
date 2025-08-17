from binance.exceptions import BinanceAPIException

def place_stop_limit_order(
    client,
    symbol: str,
    side: str,
    quantity: float,
    stop_price: float,
    limit_price: float,
    time_in_force="GTC",
):
    """
    Places a Stop-Limit order.
    When stop_price is reached, it triggers a LIMIT order at limit_price.
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP",
            quantity=quantity,
            price=limit_price,
            stopPrice=stop_price,
            timeInForce=time_in_force,
            workingType="MARK_PRICE"
        )
        return order
    except BinanceAPIException as e:
        raise Exception(f"Stop-Limit order failed: {str(e)}")
