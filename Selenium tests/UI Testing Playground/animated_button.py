from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://uitestingplayground.com/animation"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Animated Button']"))
)

animation_button = driver.find_element(By.ID, "animationButton")
moving_target = driver.find_element(By.ID, "movingTarget")

animation_button.click()

WebDriverWait(driver, 60).until(
    lambda d: "spin" not in d.find_element(By.ID, "movingTarget").get_attribute("class")
)

moving_target.click()

status = driver.find_element(By.ID, "opstatus")
print(status.text)

sleep(10)

driver.quit()