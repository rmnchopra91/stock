# pip install dhanhq
# pip install websockets
from dhanhq import dhanhq
from dhanhq import marketfeed

import constant as cons

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA4MDgxNTk4LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjQ2ODY5MiJ9.ZGIxqrE5ODPO_HYSy4yNET0Er7PoHHE-cT-IOgWzVsZbyjfxFy2nf_9u-WNwGU0JJLIHv5OTlNv14BGv_Raziw"
client_id = "1102468692"


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
    print(hdfc_order)

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