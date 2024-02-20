import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import os
from concurrent.futures import ThreadPoolExecutor

class AsyncImageDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Downloader")
        self.geometry("500x400")

        self.downloading = False
        self.executor = ThreadPoolExecutor(max_workers=5)

        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = ttk.Label(self, text="Image Downloader", font=("Arial", 20, "bold"))
        header_label.pack(pady=10)

        # URL Entry and Download Button
        url_frame = ttk.Frame(self)
        ttk.Label(url_frame, text="URL: ").pack(side=tk.LEFT)

        self.url_entry = ttk.Entry(url_frame, width=30)
        self.url_entry.pack(side=tk.LEFT, padx=5)

        download_icon = tk.PhotoImage(file="download.png")
        self.download_button = ttk.Button(url_frame, text="Download", image=download_icon, compound=tk.RIGHT,
                                          command=self.start_download)
        self.download_button.photo = download_icon
        self.download_button.pack(side=tk.LEFT)

        url_frame.pack(pady=10)

        # Log Area
        self.log_area = tk.Text(self, height=8, state=tk.DISABLED)
        self.log_area.pack(fill=tk.BOTH, expand=True)

        # Image Display
        self.image_label = ttk.Label(self)
        self.image_label.pack(fill=tk.BOTH, expand=True)

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            self.log_message("Please enter a URL.")
            return

        if self.downloading:
            self.log_message("Already downloading. Please wait.")
            return

        self.downloading = True
        self.log_message(f"Downloading images from: {url}")

        self.executor.submit(self.download_image, url)

    def log_message(self, message):
        self.log_area.configure(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.configure(state=tk.DISABLED)
        self.log_area.see(tk.END)

    def download_image(self, url):
        try:
            image_data = urlopen(url).read()

            # Extract file name from URL
            file_name = os.path.basename(url)
            # Replace invalid characters in file name
            file_name = ''.join(c if c.isalnum() or c in ('.', '-') else '_' for c in file_name)

            file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)

            with open(file_path, 'wb') as file:
                file.write(image_data)

            self.log_message(f"Image downloaded: {file_name}")

            # Display the downloaded image
            self.display_image(file_path)
        except Exception as e:
            self.log_message(f"Error downloading image: {str(e)}")
        finally:
            self.downloading = False
            self.url_entry.delete(0, tk.END)

    def display_image(self, file_path):
        try:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.log_message(f"Error displaying image: {str(e)}")

if __name__ == "__main__":
    app = AsyncImageDownloader()
    app.mainloop()
