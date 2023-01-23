import tkinter as tk
from tkinter import messagebox
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Global variables
driver = webdriver.Safari()

def upload_watchlist():
    messagebox.showinfo("Watchlist Manager", "Uploading watchlist...")

def submit_login_info(username, password, window):
    try:
        #clicked sign-in
        element = driver.find_element(By.XPATH, '//*[@id="imdbHeader"]/div[2]/div[5]/a')
        driver.get(element.get_attribute("href"))
        window.destroy()

        #clicking login with imdb
        wait = WebDriverWait(driver, 10)
        imdbElement = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin-options"]/div/div[1]/a[1]')))
        driver.get(imdbElement.get_attribute("href"))

        #populate the username and password field
        # locate the element
        wait = WebDriverWait(driver, 10)
        emailElement = wait.until(EC.visibility_of_element_located((By.ID, "ap_email")))
        passwordElement = wait.until(EC.visibility_of_element_located((By.ID, "ap_password")))

        # input text into the elements
        emailElement.send_keys(username)
        passwordElement.send_keys(password)

        #click submit
        submitElement = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "a-button-input")))
        submitElement.submit()
        
    except Exception as e:
        print("An error occurred: ", e)

def create_login_GUI():
    # Create a new window
    window = Tk()
    window.title("IMDb Login")

    # Create a label for the username
    username_label = Label(window, text="Username:")
    username_label.pack()

    # Create an entry field for the username
    username_entry = Entry(window)
    username_entry.pack()

    # Create a label for the password
    password_label = Label(window, text="Password:")
    password_label.pack()

    # Create an entry field for the password
    password_entry = Entry(window, show="*")
    password_entry.pack()

    # Create a submit button
    submit_button = Button(window, text="Submit", command=lambda: submit_login_info(username_entry.get(), password_entry.get(), window))
    submit_button.pack()

    # Run the window
    window.mainloop()


def download_watchlist():
    # Navigate to the IMDb website
    driver.get("https://www.imdb.com/")

    wait = WebDriverWait(driver, 10)
    loginElement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="imdbHeader"]/div[2]/div[5]/a/div')))
    
    if loginElement.text == 'Sign In':
        create_login_GUI()
    else:
        print("The text is 'Sign In'")

    # Close the browser
    # driver.quit()

def create_GUI():
    root = tk.Tk()
    root.title("Watchlist Manager")

    upload_button = tk.Button(root, text="Upload your watchlist", command=upload_watchlist)
    upload_button.pack()

    download_button = tk.Button(root, text="Download your watchlist", command=download_watchlist)
    download_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_GUI()
