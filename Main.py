import tkinter as tk
from tkinter import messagebox
from selenium import webdriver

def upload_watchlist():
    messagebox.showinfo("Watchlist Manager", "Uploading watchlist...")

def download_watchlist():
    messagebox.showinfo("Watchlist Manager", "Downloading watchlist...")

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
