from dhanhq import marketfeed
import csv

# Add your Dhan Client ID and Access Token
client_id = "client_id"
access_token = "access_token"

# Structure for subscribing is ("exchange_segment","security_id")

# Maximum 100 instruments can be subscribed, then use 'subscribe_symbols' function 

instruments = [(0,"25"), (1, 13)]

# Type of data subscription
subscription_code = marketfeed.Quote

# Ticker - Ticker Data
# Quote - Quote Data
# Depth - Market Depth


async def on_connect(instance):
    print("Connected to websocket")

async def on_message(instance, message):
    print("Received:", message)

    # # Write data to CSV file
    # with open('data.csv', 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(message.keys())
    #     for row in zip(*[ [v] for v in message.values() ]):
    #         writer.writerow(row)
    # Write data to CSV file
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for row in zip(*[ [v] for v in message.values() ]):
            writer.writerow(row)

print("Subscription code :", subscription_code)

# Write the keys to the CSV file
field_names = ['type', 'exchange_segment', 'security_id', 'LTP', 'LTQ', 'LTT', 'avg_price', 'volume', 'total_sell_quantity', 'total_buy_quantity', 'open', 'close', 'high', 'low']
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(field_names)

feed = marketfeed.DhanFeed(client_id,
    access_token,
    instruments,
    subscription_code,
    on_connect=on_connect,
    on_message=on_message)

feed.run_forever()