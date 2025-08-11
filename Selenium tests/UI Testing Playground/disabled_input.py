from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://uitestingplayground.com/disabledinput"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Disabled Input']"))
)

button = driver.find_element(By.ID, "enableButton")
button.click()

input_field = WebDriverWait(driver, 5).until(
    # waits until input_field is enabled again 5 seconds after button click
    lambda d: d.find_element(By.ID, "inputField") if d.find_element(By.ID, "inputField").is_enabled() else False
)

input_field.send_keys("aaaaaaaaaaaaa")

sleep(5)

driver.quit()