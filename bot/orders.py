from bot.client import client


# MARKET ORDER
def place_market_order(symbol, side, quantity):

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        return order

    except Exception as e:
        raise e


# LIMIT ORDER
def place_limit_order(symbol, side, quantity, price):

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        return order

    except Exception as e:
        raise e
