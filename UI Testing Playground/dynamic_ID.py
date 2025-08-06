from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/dynamicid"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

driver.execute_script("""
    window.clicked = false;
    const button = document.querySelector("button.btn.btn-primary");
    if (button) {
        button.addEventListener("click", () => { window.clicked = true; });
    }
""")

button_with_dynamic_id = WebDriverWait(driver, 10).until(
    # EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    # EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Button with Dynamic ID']"))
)
button_with_dynamic_id.click()

clicked = driver.execute_script("return window.clicked;")

if clicked:
    print("Button was successfully clicked.")
else:
    print("Button click not detected.")

driver.quit()