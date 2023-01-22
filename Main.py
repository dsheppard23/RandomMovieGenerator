import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import time

def upload_watchlist():
    messagebox.showinfo("Watchlist Manager", "Uploading watchlist...")

def download_watchlist():
    # Create a new instance of the Safari driver
    driver = webdriver.Safari()

    # Navigate to the IMDb website
    driver.get("https://www.imdb.com/")

    #wait for the page to load
    time.sleep(5)
    # Code to log in and download the watchlist goes here
    
    # Close the browser
    driver.quit()


def CreateGUI():
    root = tk.Tk()
    root.title("Watchlist Manager")

    upload_button = tk.Button(root, text="Upload your watchlist", command=upload_watchlist)
    upload_button.pack()

    download_button = tk.Button(root, text="Download your watchlist", command=download_watchlist)
    download_button.pack()

    root.mainloop()

if __name__ == "__main__":
    CreateGUI()
