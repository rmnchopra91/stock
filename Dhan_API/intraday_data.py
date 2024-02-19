import requests
import csv
import json
from datetime import datetime, timedelta

url = "https://api.dhan.co/charts/intraday"

payload = {
    "securityId": "500285",
    "exchangeSegment": "BSE_EQ",
    "instrument": "EQUITY"
}

headers = {
    "access-token": "access-token",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def convert_to_date_time(JulianDate):
        """Convert julian date to python datetime object"""
        Dt1980= datetime(year=1980,month=1,day=1,hour=5,minute=30)
        DtObj= Dt1980+ timedelta(seconds=JulianDate)
        return DtObj

try:
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # # Convert start_Time to datetime and add as a new column
        start_time = [convert_to_date_time(t) for t in data['start_Time']]
        dates = [t for t in start_time]
        data['date'] = dates

        with open('intraday_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data.keys())
                for row in zip(*data.values()):
                    writer.writerow(row)

        print("Data saved to intraday_data.csv")

    else:
        print(f"Error: Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")