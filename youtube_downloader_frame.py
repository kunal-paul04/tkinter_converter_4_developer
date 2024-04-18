import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import validators

class YoutubeDownloaderFrame(tk.Frame):
    def __init__(self, parent, main_page, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main_page = main_page

        self.grid(row=0, column=0, sticky="nsew")

        self.header_label = tk.Label(self, text="YouTube Video Downloader [in highest video quality available (720p Max)]", font=("Calibari", 16, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=4, pady=(50, 20))

        self.entry_label = tk.Label(self, text="Enter YouTube video URL:", font=("Calibari", 12))
        self.entry_label.grid(row=1, column=0, padx=10)

        self.entry_url = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_url, width=50)
        self.entry.grid(row=1, column=1, padx=10)
        self.entry.bind('<Button-1>', self.on_entry_click)  # Bind placeholder behavior

        self.download_button = tk.Button(self, text="Download", command=self.download_video, font=("Calibari", 12, "bold"))
        self.download_button.grid(row=1, column=2, padx=10)

        self.back_button = tk.Button(self, text="Back to Home", command=self.back_to_home, font=("Calibari", 12, "bold"))
        self.back_button.grid(row=1, column=3, pady=10)

        self.output_label = tk.Label(self, text="", font=("Calibari", 12), wraplength=600)
        self.output_label.grid(row=2, column=0, columnspan=3, pady=20)

        self.clear_error()  # Clear any previous error messages

        # Animation variables
        self.waiting_message_flag = False
        self.dot_count = 0

    def back_to_home(self):
        self.main_page.tkraise()  # Raise the main frame

    def download_video(self):
        link = self.entry_url.get()
        try:
            # Validate the URL
            if not validators.url(link):
                raise ValueError("Invalid URL")

            # Ask user for save location
            folder_path = filedialog.askdirectory()
            if not folder_path:
                # User canceled the operation
                return

            # Show "Fetching video..." message
            self.output_label.config(text="Fetching video...")
            self.update()

            # Perform conversion
            video = YouTube(link)
            streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            highest_resolution = streams.first().resolution
            video_title = video.title
            video_resolution = video.streams.get_highest_resolution()

            # Show "Downloading..." message
            self.output_label.config(text="Downloading...")
            self.update()

            # Start waiting message animation
            self.waiting_message_flag = True
            self.animate_waiting_message()

            # Download the video to the folder
            video_resolution.download(output_path=folder_path)

            # Stop waiting message animation
            self.stop_animation()

            # Display video information
            self.output_label.config(text="Video Title: {}\nVideo Resolution: {}\n\nVideo Downloaded Successfully...".format(video_title, highest_resolution))
        except Exception as e:
            self.output_label.config(text="Error: {}".format(str(e)))

    def clear_error(self):
        self.output_label.config(text="")

    def animate_waiting_message(self):
        if self.waiting_message_flag:
            self.output_label.config(text="Fetching video" + "." * self.dot_count)
            self.after(500, self.animate_waiting_message)

    def stop_animation(self):
        self.waiting_message_flag = False

    def on_entry_click(self, event):
        if self.entry.get() == 'Enter YouTube video URL':
            self.entry.delete(0, "end")  # Delete all the text in the entry
            self.entry_style.configure('Placeholder.TEntry', foreground='black')  # Change text color to black
