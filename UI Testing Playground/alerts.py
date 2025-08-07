from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from time import sleep

url = "https://uitestingplayground.com/alerts"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Alerts']"))
)

alert_button = driver.find_element(By.ID, "alertButton")
alert_button.click()
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.accept()

sleep(3)

confirm_button = driver.find_element(By.ID, "confirmButton")
confirm_button.click()
day_of_week_name = datetime.datetime.today().strftime('%A')
print(day_of_week_name)
wait = WebDriverWait(driver, timeout=2)
alert = wait.until(lambda d : d.switch_to.alert)
if day_of_week_name != "Friday":
    alert.dismiss()
else:
    alert.accept()
# additional alert
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.accept()

sleep(3)

prompt_button = driver.find_element(By.ID, "promptButton")
prompt_button.click()
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.send_keys("cats")
alert.accept()
sleep(3)
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.accept()

sleep(5)

driver.quit()