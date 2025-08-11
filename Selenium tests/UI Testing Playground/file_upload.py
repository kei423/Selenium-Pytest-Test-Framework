from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

url = "https://uitestingplayground.com/upload"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='File Upload']"))
)

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "UI Testing Playground\\a.txt"))

# manual browse and upload
file_input = driver.find_element(By.ID, "browse")
file_input.send_keys(upload_file)

sleep(10)

driver.quit()