from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://uitestingplayground.com/textinput"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

new_button_name = "New Button Name nihihi"

text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "newButtonName"))
)
text.send_keys(new_button_name)

button = driver.find_element(By.ID, "updatingButton")
# grabs old name
old_button_name = button.text
button.click()

updated_button = driver.find_element(By.XPATH, f"//button[text()='{new_button_name}']")
# grabs new name
updated_name = updated_button.text

assert old_button_name is not updated_name, "Button name wasn't changed"

print("Button name was sucessfully changed")

driver.quit()