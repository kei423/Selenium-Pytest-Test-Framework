from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from common_functions import create_user, verify_username_is_visible, delete_account
import time

# create the user before logging in
# assuming credentials are
# email: testemail423@gmail.com
# password: !23456A@
# create_user()

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service) # launch browser

driver.get("http://automationexercise.com") # navigate to url

WebDriverWait(driver, 5).until(
    # verify that home page is visible
    EC.presence_of_element_located((By.XPATH, "//img[@alt='Website for automation practice']"))
)

# click on 'Signup / Login' button
login_signup_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Signup / Login')]"))
)
login_signup_button.click()

WebDriverWait(driver, 5).until(
    # verify 'Login to your account' is visible
    EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']"))
)

email_correct = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
email_correct.send_keys("testemail423@gmail.com")
password_correct = driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
password_correct.send_keys("!23456A@")

# click 'Login' button
login_button = driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
login_button.click()

# verify that 'Logged in as username' is visible
verify_username_is_visible(driver)

# # delete and verify that account is deleted
delete_account(driver)

time.sleep(10)

driver.quit()