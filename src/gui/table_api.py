import tkinter as tk
import requests

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
        api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Replace with your API endpoint
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            headers = ["Header 1", "Header 2", "Header 3"]  # Provide headers based on your API data
            self.table = Table(self, data, headers=headers)
            self.table.pack(expand=True, fill="both")
        else:
            print("Failed to fetch data from API.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
