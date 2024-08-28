import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import pyautogui

# Function to send email
def send_email():
    your_email = email_entry.get()
    reciever_email = receiver_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    # Initialize undetected chromedriver
    options = uc.ChromeOptions()
    options.headless = False
    driver = uc.Chrome(version_main=127, options=options, use_subprocess=True)
    driver.maximize_window()

    try:
        # Open the Gmail page
        driver.get("https://www.google.com/intl/en-US/gmail/about/")
        pyautogui.click()

        # Wait for the button to be clickable and then click it
        wait = WebDriverWait(driver, 20)  # wait for up to 20 seconds
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button--mobile-before-hero-only")))
        button.click()

        # Check if we're on the AccountChooser page and wait for the next button if it exists
        if "AccountChooser" in driver.current_url:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Сменить аккаунт")]')))
            next_button.click()

        # Wait for the email input field and enter the email
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
        email_input.send_keys(your_email)
        email_input.send_keys(Keys.RETURN)

        # Wait for the password input field and enter the password
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Wait for the "Compose" button to appear and click it
        write_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Compose")]')))
        write_button.click()

        # Use pyautogui to type in the recipient's email
        time.sleep(2)  # slight delay before typing
        pyautogui.write(reciever_email)
        time.sleep(2)

        # Wait for the subject input field and enter the subject
        msg_subject = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Subject"]')))
        msg_subject.send_keys(subject)

        # Wait for the email body to be clickable and click to focus
        message_body = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.Ap div[g_editable="true"]')))
        message_body.click()

        # Use pyautogui to type the message
        pyautogui.write(body)

        # Wait for the send button to be clickable and click it
        send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-tooltip-delay="800"]:nth-child(1)')))
        send_button.click()

        # Keep the browser open to observe the results
        time.sleep(3)
        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        driver.save_screenshot("screenshot.png")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    finally:
        driver.quit()

# Create the main window
root = tk.Tk()
root.title("Gmail Automation")

# Create labels and entries for user input
tk.Label(root, text="Your Email:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Receiver Email:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
receiver_entry = tk.Entry(root, width=40)
receiver_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Subject:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
subject_entry = tk.Entry(root, width=40)
subject_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Body:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
body_text = tk.Text(root, height=10, width=40)
body_text.grid(row=4, column=1, padx=5, pady=5)

# Create a send button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
