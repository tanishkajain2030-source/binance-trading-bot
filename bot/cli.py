
import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


# Create parser
parser = argparse.ArgumentParser()

# CLI arguments
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

# Read arguments
args = parser.parse_args()


try:

    # Validate inputs
    symbol = args.symbol.upper()

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    price = validate_price(args.price, order_type)


    # MARKET ORDER
    if order_type == "MARKET":

        order = place_market_order(
            symbol,
            side,
            quantity
        )
    


    # LIMIT ORDER
    elif order_type == "LIMIT":

        order = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )


    # Print response
    print("\nOrder Placed Successfully\n")

    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Quantity:", order.get("executedQty"))


    # Logging
    logger.info(f"{side} {order_type} order placed for {symbol}")


except Exception as e:

    print("\nError:")
    print(e)

    logger.error(str(e))