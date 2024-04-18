import tkinter as tk
from tkinter import filedialog

class SQLConverterFrame(tk.Frame):
    def __init__(self, parent, main_page, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main_page = main_page

        self.grid(row=0, column=0, sticky="nsew")

        self.header_label = tk.Label(self, text="Convert excel (xlsx) to SQL", font=("Calibari", 16, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=5, pady=(50, 20))

        self.entry_label = tk.Label(self, text="Add excel file:", font=("Calibari", 12))
        self.entry_label.grid(row=1, column=0, padx=10)

        self.entry_var = tk.StringVar()
        self.entry_box = tk.Entry(self, textvariable=self.entry_var, font=("Calibari", 12), state="readonly", width=40)
        self.entry_box.grid(row=1, column=1, padx=10)

        self.browse_button = tk.Button(self, text="Browse", command=self.select_file, font=("Calibari", 12, "bold"))
        self.browse_button.grid(row=1, column=2, padx=10)

        self.convert_button = tk.Button(self, text="Convert", command=self.back_to_home, font=("Calibari", 12, "bold"), width=15)
        self.convert_button.grid(row=1, column=3, padx=10)

        self.back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, font=("Calibari", 12, "bold"), width=15)
        self.back_button.grid(row=1, column=4, padx=10, pady=20, sticky='e')

    def back_to_home(self):
        self.main_page.tkraise()  # Raise the main frame

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.entry_var.set(file_path)  # Set the selected file path in the entry box

