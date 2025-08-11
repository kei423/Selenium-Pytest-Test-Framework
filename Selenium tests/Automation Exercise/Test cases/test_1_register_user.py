from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

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
    # verify 'Enter Account Information' is visible
    EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']"))
)

# fill details; title, name, email, password, date of birth
title_element = driver.find_element(By.ID, 'id_gender1')
title_element.click()

# name and email are already filled in
# name_element = driver.find_element(By.ID, "//input[@data-qa='name']")
# name_element.send_keys("testUser423")
# email_element = driver.find_element(By.XPATH, "//input[@data-qa='email']")
# email_element.send_keys("testemail423@gmail.com")

password_element = driver.find_element(By.XPATH, "//input[@data-qa='password']")
password_element.send_keys("!23456A@")
select_day = Select(driver.find_element(By.ID, "days"))
select_day.select_by_value("7")
select_month = Select(driver.find_element(By.ID, "months"))
select_month.select_by_value("5")
select_year = Select(driver.find_element(By.ID, "years"))
select_year.select_by_value("1996")

# select checkbox 'Sign up for our newsletter!'
newsletter_element = driver.find_element(By.ID, "newsletter")
newsletter_element.click()

# select checkbox 'Receive special offers from our partners!'
offer_element = driver.find_element(By.ID, "optin")
offer_element.click()

# fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
first_name = driver.find_element(By.ID, "first_name")
first_name.send_keys('Abcdef')
last_name = driver.find_element(By.ID, "last_name")
last_name.send_keys('Vwxyz')
company_name = driver.find_element(By.ID, "company")
company_name.send_keys("K423 HQ")
address1 = driver.find_element(By.ID, "address1")
address1.send_keys("123 1st Street")
address2 = driver.find_element(By.ID, "address2")
address2.send_keys("456 2nd Street")
select_country = Select(driver.find_element(By.ID, "country"))
select_country.select_by_value("United States")
state = driver.find_element(By.ID, "state")
state.send_keys("CA")
city = driver.find_element(By.ID, "city")
city.send_keys("New York")
zipcode = driver.find_element(By.ID, "zipcode")
zipcode.send_keys("12345")
mobile_number = driver.find_element(By.ID, "mobile_number")
mobile_number.send_keys("123")

# click 'Create Account' button
create_account_button = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
create_account_button.click()

WebDriverWait(driver, 10).until(
    # verify 'Account Created!' is visible
    EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
)

# click 'Create Account button'
continue_button = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
continue_button.click()

WebDriverWait(driver, 10).until(
    # verify that 'Logged in as username' is visible
    EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Logged in as testUser423')]"))
)

# click 'Delete Account button'
delete_account_button = driver.find_element(By.XPATH, "//a[contains(text(), ' Delete Account')]")
delete_account_button.click()

# verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']"))
)
continue_button = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
continue_button.click()

time.sleep(10)

driver.quit()