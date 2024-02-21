import tkinter as tk
import requests

from historical_data import get_historical_data

class Table(tk.Frame):
    def __init__(self, parent, data, headers=[], *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data = data
        self.headers = headers
        self.create_widgets()

    def create_widgets(self):
        if self.headers:
            for column, header_text in enumerate(self.headers):
                header_label = tk.Label(self, text=header_text, borderwidth=1, relief="solid")
                header_label.grid(row=0, column=column, sticky="nsew")

        for row, item in enumerate(self.data, start=1):
            for column, value in enumerate(item):
                cell = tk.Entry(self, borderwidth=1, relief="solid", bg="white")
                cell.grid(row=row, column=column, sticky="nsew")
                cell.insert(tk.END, value)

        for row in range(len(self.data) + 1):
            self.grid_rowconfigure(row, weight=1)

        for column in range(len(self.headers)):
            self.grid_columnconfigure(column, weight=1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Table with API Data")

        # Fetch data from API
        url = "https://api.dhan.co/charts/historical"  # Replace with your API endpoint
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
        response = requests.post(url, json=payload, headers=headers)
        # response = data.get_historical_data()
        if response.status_code == 200:
            data = response.json()
            headers = ["open","high","low","close","volume","start_Time","date"]  # Provide headers based on your API data
            self.table = Table(self, data, headers=headers)
            self.table.pack(expand=True, fill="both")
        else:
            print("Failed to fetch data from API.")

    def test(self):
        print("this is my test funtion")

if __name__ == "__main__":
    # url = "https://api.dhan.co/charts/historical"

    # print(get_historical_data(url, payload, headers, csv_filename))
    app = App()
    app.mainloop()
    app.test()
