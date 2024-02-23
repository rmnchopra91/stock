import requests
import json
import csv
from datetime import datetime, timedelta


def convert_to_date_time(JulianDate):
        """Convert julian date to python datetime object"""
        Dt1980= datetime(year=1980,month=1,day=1,hour=5,minute=30)
        DtObj= Dt1980+ timedelta(seconds=JulianDate)
        return DtObj

def get_historical_data(url, payload, headers):
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # # Convert start_Time to datetime and add as a new column
            start_time = [convert_to_date_time(t) for t in data['start_Time']]
            dates = [t.date() for t in start_time]
            data['date'] = dates
            # Write data to CSV file
            # with open(csv_filename, 'w', newline='') as file:
            #     writer = csv.writer(file)
            #     writer.writerow(data.keys())
            #     for row in zip(*data.values()):
            #         writer.writerow(row)

            print(f"Data saved to file.")
            return data

        else:
            print(f"Error: Request failed with status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
url = "https://api.dhan.co/charts/historical"

payload = {
    "symbol": "TCS",
    "exchangeSegment": "NSE_EQ",
    "instrument": "EQUITY",
    "expiryCode": -2147483648,
    "fromDate": "2024-01-01",
    "toDate": "2024-01-31"
}

headers = {
     "access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA4ODU3MjUwLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjQ4MzczMCJ9.KWyGKr-BL9vJ12OOhYmqcHw9S3n5w_6rYKCEc_6w9zEzVLJdjooVzl46joGbLY1ALlE_J9v_VpHVnKS9r3H5yw",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# csv_filename = 'historical_data.csv'
data = get_historical_data(url, payload, headers)
# print(json.dumps(data, indent=4))








# from dhanhq import dhanhq
# import pandas as pd
# import csv

# def get_historical_data_and_store_in_csv(client_id, access_token, symbol, exchange_segment, instrument_type, expiry_code, from_date, to_date, csv_filename):
#     try:
#         dhan = dhanhq(client_id, access_token)

#         historical_data = dhan.historical_daily_data(
#             symbol=symbol,
#             exchange_segment=exchange_segment,
#             instrument_type=instrument_type,
#             expiry_code=expiry_code,
#             from_date=from_date,
#             to_date=to_date
#         )

#         if 'data' in historical_data:
#             historical_df = pd.DataFrame(historical_data['data'])

#             # Convert start_Time to datetime and add as a new column
#             temp_list = []
#             for i in historical_df['start_Time']:
#                 try:
#                     temp = dhan.convert_to_date_time(i)
#                     temp_list.append(temp)
#                 except Exception as e:
#                     print(f"Error: {e}")

#             historical_df['date'] = temp_list

#             # Save data to CSV file
#             historical_df.to_csv(csv_filename, index=False)
#             print(f"Data saved to {csv_filename}")

#         else:
#             print("Error: Historical data not found")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# client_id = "client_id"
# access_token = "access_token"
# symbol = 'TCS'
# exchange_segment = 'NSE_EQ'
# instrument_type = 'EQUITY'
# expiry_code = 0
# from_date = '2024-01-01'
# to_date = '2024-02-16'
# csv_filename = 'historical_data.csv'

# get_historical_data_and_store_in_csv(client_id, access_token, symbol, exchange_segment, instrument_type, expiry_code, from_date, to_date, csv_filename)





# historical_data = dhan.historical_daily_data(
#     symbol='TCS',
#     exchange_segment='NSE_EQ',
#     instrument_type='EQUITY',
#     expiry_code=0,
#     from_date='2024-01-16',
#     to_date='2024-02-16'
# )

# historical_df = pd.DataFrame(historical_data['data'])
# temp_list = []

# for i in historical_df['start_Time']:
#     temp = dhan.convert_to_date_time(i)
#     temp_list.append(temp)

# historical_df['date'] = temp_list

# print(historical_df)