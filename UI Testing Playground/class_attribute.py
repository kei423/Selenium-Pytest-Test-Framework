from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://uitestingplayground.com/classattr"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"))
)
blue_button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
time.sleep(5)
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
print("Alert accepted")

driver.quit()