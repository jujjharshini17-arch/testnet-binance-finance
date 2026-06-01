from orders import place_market_order, place_limit_order
import logging

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print("\n=== Binance Futures Testnet Bot ===\n")

symbol = input("Symbol (BTCUSDT): ").strip().upper() or "BTCUSDT"
side = input("Side (BUY/SELL): ").strip().upper()
order_type = input("Order Type (MARKET/LIMIT): ").strip().upper()
quantity = float(input("Quantity: ").strip())

if side not in ("BUY", "SELL"):
    print(f"Invalid side '{side}'. Must be BUY or SELL.")
    exit(1)

if order_type not in ("MARKET", "LIMIT"):
    print(f"Invalid order type '{order_type}'. Must be MARKET or LIMIT.")
    exit(1)

try:
    if order_type == "MARKET":
        result = place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = float(input("Price: ").strip())
        result = place_limit_order(symbol, side, quantity, price)

    print("\nOrder placed successfully!")
    print("Order ID :", result["orderId"])
    print("Symbol   :", result["symbol"])
    print("Side     :", result["side"])
    print("Type     :", result["type"])
    print("Status   :", result["status"])
    print("Quantity :", result["origQty"])

    logging.info(result)

except Exception as e:
    print(f"\nError placing order: {e}")
    logging.error(str(e))