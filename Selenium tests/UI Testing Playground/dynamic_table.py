from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/dynamictable"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='table']"))
)

headers = driver.find_elements(By.XPATH, "//div[@role='rowgroup'][1]/div[@role='row']/span")
index = 0
for i, header in enumerate(headers, 1):
    if header.text.strip() == "CPU":
        index = i
        break

cpu_cell = driver.find_element(By.XPATH, f"//div[@role='row'][span[text()='Chrome']]/span[{index}]")
print("Chrome CPU: " + cpu_cell.text)

yellow_label = driver.find_element(By.XPATH, "//p[contains(text(), 'Chrome CPU')]")
print(yellow_label.text)

assert "Chrome CPU: " + cpu_cell.text == yellow_label.text, "Dynamic table element did not match with yellow label"

driver.quit()