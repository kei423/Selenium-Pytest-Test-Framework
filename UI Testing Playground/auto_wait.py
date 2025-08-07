from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from time import sleep

url = "https://uitestingplayground.com/autowait"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Auto Wait']"))
)

combobox = Select(driver.find_element(By.ID, "element-type"))
combobox.select_by_index(2)

visible_check = driver.find_element(By.ID, "visible")
visible_check.click()

sleep(3)

apply_3 = driver.find_element(By.ID, "applyButton3")
apply_3.click()

status = driver.find_element(By.ID, "opstatus")
print(status.text)

# cannot enter text into non-visible area
# playground = driver.find_element(By.ID, "target")
# playground.send_keys("sending text to non-visible text area")

status = driver.find_element(By.ID, "opstatus")
print(status.text)

sleep(2)

combobox.select_by_index(2)
visible_check.click()
on_top_check = driver.find_element(By.ID, "ontop")
on_top_check.click()

apply_10 = driver.find_element(By.ID, "applyButton10")
apply_10.click()

sleep(3)

playground = driver.find_element(By.ID, "target")
playground.send_keys("sending text to non-on-top text area")

status = driver.find_element(By.ID, "opstatus")
print(status.text)

sleep(2)

outside_element = driver.find_element(By.TAG_NAME, "h4")  # The "Settings" header
outside_element.click()

status = driver.find_element(By.ID, "opstatus")
print(status.text)

sleep(2)

driver.quit()