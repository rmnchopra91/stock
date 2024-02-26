# pip install dhanhq
# pip install websockets
from dhanhq import dhanhq
from dhanhq import marketfeed
import logging

import constant as cons

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

access_token = ""
client_id = ""


def place_order(id, token, security_id , price):
    # dhan = dhanhq("client_id","access_token")
    dhan = dhanhq(id,token)
    hdfc_order = dhan.place_order(security_id=security_id,   #hdfcbank
        exchange_segment=dhan.NSE,
        transaction_type=dhan.BUY,
        quantity=10,
        order_type=dhan.MARKET,
        product_type=dhan.INTRA,
        price=price)
    return hdfc_order
                    
def cancel_order(id, token, order_id):
    """
    Cancel an order with the given ID.

    Parameters:
    order_id (str): The ID of the order to cancel.

    Returns:
    dict: The status of the cancelled order.

    Raises:
    dhan.DhanError: If the order cancellation fails.
    """

    # Connect to the Dhan API
    dhan = dhanhq(client_id=id, access_token=token)

    # Cancel the order
    try:
        order_status = dhan.cancel_order(order_id)
        logging.info(f"Order cancelled with status {order_status}")
        return order_status
    except Exception as e:
        logging.error(f"Error cancelling order: {e}")
        raise

def modify_order(id, token, order_id, quantity, price):
    """
    Modify an order with the given ID.

    Parameters:
    order_id (str): The ID of the order to modify.
    quantity (int): The new quantity of the security to trade.
    price (float): The new price at which to trade the security.
    order_type (str): The new type of the order (e.g. "LIMIT", "MARKET").
    validity (str): The new validity of the order (e.g. "DAY", "GOOD_TILL_CANCEL").

    Returns:
    dict: The status of the modified order.

    Raises:
    dhan.DhanError: If the order modification fails.
    """

    # Connect to the Dhan API
    dhan = dhanhq(client_id=id, access_token=token)

    # Modify the order
    try:
        order_status = dhan.modify_order(
            order_id=order_id,
            order_type=dhan.MARKET,
            leg_name='ENTRY_LEG',
            quantity=quantity,
            price=price,
            disclosed_quantity=10,
            trigger_price=0,
            validity=dhan.DAY
        )
        logging.info(f"Order modified with status {order_status}")
        return order_status
    except Exception as e:
        logging.error(f"Error modifying order: {e}")
        raise
        # return None, f"Error modifying order: {str(e)}"

def get_order_status(id, token, order_id):
    """
    Get the status of an order with the given ID.

    Parameters:
    order_id (str): The ID of the order to retrieve the status for.

    Returns:
    dict: The status of the order.

    Raises:
    dhan.DhanError: If the order status retrieval fails.
    """

    # Connect to the Dhan API
    dhan = dhanhq(client_id=id, access_token=token)

    # Retrieve the order status
    try:
        order_status = dhan.get_order_by_id(order_id)
        logging.info(f"Order status: {order_status}")
        return order_status
    except Exception as e:
        logging.error(f"Error retrieving order status: {e}")
        raise

async def on_connect(instance):
    print("Connected to websocket")

async def on_message(instance, message):
    cons.list.append(message)
    print("Received:", message)

def set_feed(security_id):
    cons.list = []
    instruments = [(1, security_id),(0,"13")]
    subscription_code = marketfeed.Ticker
    feed = marketfeed.DhanFeed(client_id, access_token,
                            instruments, 
                            subscription_code, 
                            on_connect=on_connect,
                            on_message=on_message)
    
    feed.run_forever()

# hdfc_order()