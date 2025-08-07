from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/nbsp"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Non-Breaking Space']"))
)

# fails to find the button
# button = driver.find_element(By.XPATH, "//button[text()='My Button']")

# \u00a0 is the uni-code for &nbsp; (non-breaking space)
button = driver.find_element(By.XPATH, "//button[text()='My\u00a0Button']")

driver.quit()