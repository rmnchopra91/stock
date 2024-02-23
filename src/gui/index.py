import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import threading
from dhanhq import dhanhq
from dhanhq import marketfeed
import tracemalloc
import dhan_test as api

from historical_data import get_historical_data

import tkinter as tk

class Table(tk.Frame):
    def __init__(self,  parent, data, headers=[], *args, **kwargs):
        super().__init__(parent)
        self.grid(sticky="nsew")
        self.data = data
        self.headers = headers
        self.headers = headers
        self.create_widgets()

    def create_widgets(self):
        if self.headers:
            for column, header_text in enumerate(self.headers):
                header_label = tk.Label(self, text=header_text, borderwidth=1, relief="solid")
                header_label.grid(row=0, column=column, sticky="nsew")
            
            for column, header_value in enumerate(self.data.keys()):
                for row, inner_value in enumerate(self.data[header_value][:15]):
                    cell = tk.Entry(self, borderwidth=1, relief="solid", bg="yellow")
                    cell.grid(row=row+1, column=column, sticky="nsew")
                    cell.insert(tk.END, inner_value)
        
        for row in range(len(self.data) + 1):
            self.grid_rowconfigure(row, weight=1)

        for column in range(len(self.headers)):
            self.grid_columnconfigure(column, weight=1)

class App(tk.Tk):
    # global url, payload, data, headers
    # def create_label(self, text, row, column):
    #     self.input1_label = tk.Label(self, text=text)
    #     self.input1_label.grid(row=row, column=column, padx=0, pady=10)
    
    # def create_input(self):
    #     self.input1_entry = tk.Entry(self)
    #     self.input1_entry.grid(row=0, column=1, padx=0, pady=10)

    def __init__(self):
        super().__init__()
        self.symbol = "SBIN"
        self.title("Table with Input Fields and Button")
        self.client_id = "1102483730"
        self.access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA4ODU3MjUwLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjQ4MzczMCJ9.KWyGKr-BL9vJ12OOhYmqcHw9S3n5w_6rYKCEc_6w9zEzVLJdjooVzl46joGbLY1ALlE_J9v_VpHVnKS9r3H5yw"

        self.price_label = tk.Label(self, text="Price:")
        self.price_label.grid(row=0, column=0, padx=0, pady=10)

        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=0, column=1, padx=0, pady=10)

        self.security_id_label = tk.Label(self, text="Security id:")
        self.security_id_label.grid(row=0, column=2, padx=0, pady=10)

        self.security_id_entry = tk.Entry(self)
        self.security_id_entry.grid(row=0, column=3, padx=0, pady=10)

        self.submit_button = tk.Button(self, text="place order", command=self.place_order)
        self.submit_button.grid(row=0, column=4, padx=0, pady=10)

        self.symbol_label = tk.Label(self, text="Symbol:")
        self.symbol_label.grid(row=1, column=0, padx=0, pady=10)
        self.symbol_entry = tk.Entry(self)
        self.symbol_entry.grid(row=1, column=1, padx=0, pady=10)
        # self.symbol_entry.set(self.symbol)
        self.submit_button = tk.Button(self, text="Symbol Data", command=self.get_symbol_data)
        self.submit_button.grid(row=1, column=2, padx=0, pady=10)

        self.set_label()
        self.set_table()

    def place_order(self):
        security_id = self.price_entry.get()
        price = self.price_entry.get()
        print(f":::::::::{price}::::::::::::::::::::")
        response = api.place_order(self.client_id, self.access_token, security_id, price)
        print(response)
        # dummy_data.append((price))
        messagebox.showinfo("Form Submitted", f"your order is placed {response}")

    def submit(self):
        print("Input 1:" )
        print("Input 2:" )
    
    def set_label(self):
        # self.symbol
        # Create a label for the heading
        self.heading = tk.Label(text=f"{self.symbol} related data", font=("Helvetica", 18, "bold"))
        self.heading.grid(row=2,column=0, columnspan=3, padx=0, pady=10)
    
    def set_table(self):
        url = "https://api.dhan.co/charts/historical"  # Replace with your API endpoint
        payload = {
            "symbol": self.symbol,
            "exchangeSegment": "NSE_EQ",
            "instrument": "EQUITY",
            "expiryCode": -2147483648,
            "fromDate": "2024-02-01",
            "toDate": "2024-02-15"
        }

        headers = {
            "access-token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        # data = []
        tracemalloc.start()
        data = get_historical_data(url, payload, headers)
        table_headers = ["open","high","low","close","volume","start_Time","date"]

        self.table = Table(self, data, headers=table_headers)
        self.table.grid(row=4, column=1, columnspan=5, sticky="nsew", padx=15, pady=25)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def get_symbol_data(self):
        self.symbol = self.symbol_entry.get()
        self.set_label()
        self.set_table()
        print("Input 1:", self.symbol_entry.get())
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
