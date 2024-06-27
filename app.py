from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

app = Flask(__name__)

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = './chromedriver'

# Function to run the Selenium automation script
def run_automation():
    options = Options()
    options.add_argument("--headless")  # Optional: Run Chrome in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(executable_path=CHROMEDRIVER_PATH), options=options)
    
    try:
        # Example automation script (replace with your logic)
        driver.get('https://web.snapchat.com/')
        sleep(10)

        Capture_Open_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/button[1]')
        Capture_Open_button.click()

        sleep(10)
        Capture_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/button[1]')
        Capture_button.click()

        sleep(3)
        sendTO_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/button[2]')
        sendTO_button.click()

        sleep(3)
        Streak_button = driver.find_element('xpath', '/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/div[2]/button')
        Streak_button.click()

        sleep(3)
        from selenium.common.exceptions import NoSuchElementException

        i = 2  # Starting index
        while True:
            try:
                xpath = f'/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/ul/li[{i}]/div/div[2]/div'
                select_ppl_button = driver.find_element('xpath', xpath)
                select_ppl_button.click()
                i += 1  # Increment the index
            except NoSuchElementException:
                # If no more elements are found, exit the loop
                break

        sleep(3)
        final_send = driver.find_element('xpath','/html/body/main/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button/div')
        final_send.click()
    finally:
        driver.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Validate login credentials here (e.g., check against a database)
    # Example: if username == 'correct_username' and password == 'correct_password':
    if True:  # Replace with actual validation logic
        run_automation()  # Call your Selenium automation script
        return render_template('dashboard.html')  # Redirect to dashboard or success page
    else:
        return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for development
