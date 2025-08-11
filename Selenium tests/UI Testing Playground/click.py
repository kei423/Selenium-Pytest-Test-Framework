from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/click"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Button That Ignores DOM Click Event']"))
)
button.click()

# green_button = driver.find_element(By.XPATH, "//button[@class='btn-success']")
green_button = driver.find_element(By.XPATH, "//button[@id='badButton']")
green_button.click()

assert "btn-success" in green_button.get_attribute("class"), "Button wasn't clickable after first click"

print("Button turned green and was clickable")

driver.quit()