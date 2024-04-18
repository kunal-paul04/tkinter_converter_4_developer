'''
    This is a tkinter app for developers. You can convert csv file into sql file, doc into pdf, and more!
'''
import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from sql_converter_frame import SQLConverterFrame
from youtube_downloader_frame import YoutubeDownloaderFrame

window = ttk.Window(themename='journal')

fontHeaderStyle = font.Font(size=16, family='Calibari', weight='bold')
fontButtonStyle = font.Font(size=14)

mainConverterPage = tk.Frame(window)
sqlConverterPage = SQLConverterFrame(window, mainConverterPage)
youtubeDownloaderPage = YoutubeDownloaderFrame(window, mainConverterPage)

mainConverterPage.grid(row=0, column=0, sticky="nsew")

mainConverterPageLabel = tk.Label(mainConverterPage, text="Super Widget - Single standalone widget for multiple work", font=fontHeaderStyle)
mainConverterPageLabel.grid(row=0, column=0, columnspan=2, pady=(50, 20))

sqlConverterButton = tk.Button(mainConverterPage, text="Convert to SQL", command=lambda: sqlConverterPage.tkraise(), font=fontButtonStyle, width=20)
sqlConverterButton.grid(row=1, column=0, padx=50, pady=20)

youtubeDownloaderButton = tk.Button(mainConverterPage, text="Download Youtube Video", command=lambda: youtubeDownloaderPage.tkraise(), font=fontButtonStyle, width=20)
youtubeDownloaderButton.grid(row=1, column=1, padx=50, pady=20)

mainConverterPage.columnconfigure(0, weight=1)  # Make column 0 expandable
mainConverterPage.columnconfigure(1, weight=1)  # Make column 1 expandable

mainConverterPage.tkraise()  # Raise mainConverterPage initially

window.title('Super Converter for Developers')  # title of window box
window.geometry('1150x600')  # widthxheight
window.resizable(False, False)  # non-resizeable window
# Run
window.mainloop()