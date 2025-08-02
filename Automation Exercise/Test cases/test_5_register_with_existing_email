from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from common_functions import create_user
import time

# create the user before logging in
# assuming credentials are
# email: testemail423@gmail.com
# password: !23456A@
# create_user()
# in this case, assuming the user already exists

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
    # verify 'New User Signup!' is visible
    EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']"))
)

# enter name and email address
name_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")
name_input.send_keys("testUser423")
email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
email_input.send_keys("testemail423@gmail.com")

# click 'Signup' button
signup_button = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
signup_button.click()

WebDriverWait(driver, 10).until(
    # verify error 'Email Address already exist!' is visible
    EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Email Address already exist!')]"))
)

print("success!")

time.sleep(10)

driver.quit()