from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

url = "https://uitestingplayground.com/shadowdom"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h3[text()='Shadow DOM']"))
)

# must first enter the root of the shadow DOM to gain access to the elements inside
shadow_host = driver.find_element(By.CSS_SELECTOR, "guid-generator")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

button_generate = shadow_root.find_element(By.ID, "buttonGenerate")
button_generate.click()

button_copy = shadow_root.find_element(By.ID, "buttonCopy")
button_copy.click()

copied_text = pyperclip.paste()

edit_field = shadow_root.find_element(By.ID, "editField")

print(copied_text)
print(edit_field.get_attribute("value"))

assert copied_text == edit_field.get_attribute("value"), "The generated text and input field text are not the same"

driver.quit()