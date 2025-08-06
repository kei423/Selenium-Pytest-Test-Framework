from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://uitestingplayground.com/scrollbars"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "hidingButton"))
)

# arguments[0] grabs the button element here
driver.execute_script("arguments[0].scrollIntoView();", button)

button.click()

time.sleep(10)

driver.quit()