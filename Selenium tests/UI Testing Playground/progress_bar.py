from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/progressbar"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "startButton"))
)

stop_button = driver.find_element(By.ID, "stopButton")

progress_bar = driver.find_element(By.ID, "progressBar")

start_button.click()

WebDriverWait(driver, 120).until(
    lambda d: int(d.find_element(By.ID, "progressBar").get_attribute("aria-valuenow")) >= 75
)

stop_button.click()

print(progress_bar.get_attribute("aria-valuenow"))
result = driver.find_element(By.ID, "result")
print(result.text)

driver.quit()