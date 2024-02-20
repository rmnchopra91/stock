import tkinter as tk
from tkinter import ttk
import sqlite3
import threading
from dhanhq import dhanhq
from dhanhq import marketfeed

import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent,headers=[], rows=10, columns=3):
        super().__init__(parent)
        self.grid(sticky="nsew")
        self.headers = headers
        self.rows = rows
        self.columns = columns
        self.create_widgets()

    def create_widgets(self):
        if self.headers:
            for column, header_text in enumerate(self.headers):
                header_label = tk.Label(self, text=header_text, borderwidth=1, relief="solid")
                header_label.grid(row=0, column=column, sticky="nsew")
            for column in range(len(self.headers), self.columns):
                header_label = tk.Label(self, text="", borderwidth=1, relief="solid")
                header_label.grid(row=0, column=column, sticky="nsew")
        
        self.cells = {}
        for row in range(self.rows):
            for column in range(self.columns):
                cell = tk.Entry(self, borderwidth=0.5, relief="solid", bg="#f5f5dc")
                cell.grid(row=row, column=column, sticky="nsew")
                self.cells[(row, column)] = cell

        for row in range(self.rows):
            self.grid_rowconfigure(row, weight=1)

        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Table with Input Fields and Button")

        self.input1_label = tk.Label(self, text="Input 1:")
        self.input1_label.grid(row=0, column=0)

        self.input1_entry = tk.Entry(self)
        self.input1_entry.grid(row=0, column=1)

        self.input2_label = tk.Label(self, text="Input 2:")
        self.input2_label.grid(row=0, column=2)

        self.input2_entry = tk.Entry(self)
        self.input2_entry.grid(row=0, column=3)

        self.input3_label = tk.Label(self, text="Input 3:")
        self.input3_label.grid(row=0, column=4)

        self.input3_entry = tk.Entry(self)
        self.input3_entry.grid(row=0, column=5)

        self.input4_label = tk.Label(self, text="Input 4:")
        self.input4_label.grid(row=0, column=6)

        self.input4_entry = tk.Entry(self)
        self.input4_entry.grid(row=0, column=7)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=0, column=8)

        self.headers = ["Header 1", "Header 2", "Header 3", "Header 3"]  # Add your header names here

        self.table = Table(self)
        self.table.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=15)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def submit(self):
        input1_value = self.input1_entry.get()
        input2_value = self.input2_entry.get()
        print("Input 1:", input1_value)
        print("Input 2:", input2_value)

if __name__ == "__main__":
    app = App()
    app.mainloop()
