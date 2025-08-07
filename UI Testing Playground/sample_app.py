from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/sampleapp"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Sample App']"))
)

username = driver.find_element(By.XPATH, "//input[@name='UserName']")
username.send_keys("aaa")
password = driver.find_element(By.XPATH, "//input[@name='Password']")
password.send_keys("pwd")
login_button = driver.find_element(By.ID, "login")
login_button.click()

login_status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "loginstatus"))
)
print(login_status.text)

driver.quit()