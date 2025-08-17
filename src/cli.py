import argparse
from basic_bot import BasicBot
from market_orders import place_market_order
from limit_orders import place_limit_order
from logger import get_logger
from advanced.stop_limit import place_stop_limit_order

logger = get_logger()

def parse_input():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")

    parser.add_argument("--api_key", required=False, help="Binance API Key")
    parser.add_argument("--api_secret", required=False, help="Binance API Secret")
    parser.add_argument("--symbol", required=True, help="Trading Symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT", "STOP_LIMIT"],
        help="Order type"
    )
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Limit price (LIMIT or STOP_LIMIT)")
    parser.add_argument("--stop_price", type=float, help="Stop trigger price (STOP_LIMIT)")
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Simulate order without sending request to Binance"
    )

    return parser.parse_args()

def main():
    args = parse_input()

    # Only create a client if dry_run = False. Otherwise, skip client creation.
    client = None
    if not args.dry_run:
        if not args.api_key or not args.api_secret:
            raise ValueError("API key and secret are required unless --dry_run is used.")
        bot = BasicBot(args.api_key, args.api_secret)
        client = bot.get_client()

    try:
        if args.type == "MARKET":
            result = place_market_order(
                client, args.symbol, args.side, args.quantity, dry_run=args.dry_run
            )

        elif args.type == "LIMIT":
            if not args.price:
                raise ValueError("Limit order requires --price.")
            result = place_limit_order(
                client, args.symbol, args.side, args.quantity, args.price, dry_run=args.dry_run
            )

        elif args.type == "STOP_LIMIT":
            if not args.price or not args.stop_price:
                raise ValueError("STOP_LIMIT order requires --price and --stop_price.")
            result = place_stop_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.stop_price,
                args.price,
                dry_run=args.dry_run
            )

        logger.info(f"Order placed: {result}")
        if args.dry_run:
            print("✅ DRY RUN: no API call made")
        else:
            print("✅ Order successfully placed")
        print(result)

    except Exception as e:
        logger.error(f"Failed to place order: {str(e)}")
        print("❌ Error:", e)

if __name__ == "__main__":
    main()