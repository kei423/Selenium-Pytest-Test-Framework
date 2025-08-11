from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://uitestingplayground.com/overlapped"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Overlapped Element']"))
)

# in the case of overlapped elements
# if text is entered before scrolling, no text will enter the field
name = driver.find_element(By.ID, "name")
# uncomment this will not enter text properly
# name.send_keys("aaaa")

driver.execute_script("arguments[0].scrollIntoView();", name)
# if text is entered after scroll, text will enter the field as intended
name.send_keys("aaaa")

sleep(10)

driver.quit()