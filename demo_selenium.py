from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Enter username
username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

# Enter password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauc")

# Click login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for a few seconds to see the result
time.sleep(5)

driver.quit()