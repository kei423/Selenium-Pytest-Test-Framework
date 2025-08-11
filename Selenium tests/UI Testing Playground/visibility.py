from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

url = "https://uitestingplayground.com/visibility"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

hide_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "hideButton"))
)

def check_button_visibility(button_id, button_name):
    try:
        button = driver.find_element(By.ID, button_id)
        if button.is_displayed():
            print(f"{button_name} still visible")
        else:
            print(f"{button_name} no longer visible")
    except NoSuchElementException as e:
        print(f"{button_name} not found")

hide_button.click()

check_button_visibility("removedButton", "Removed Button")
check_button_visibility("zeroWidthButton", "Zero Width Button")
check_button_visibility("overlappedButton", "Overlapped Button")
check_button_visibility("transparentButton", "Transparent Button")
check_button_visibility("invisibleButton", "Visibility Hidden Button")
check_button_visibility("notdisplayedButton", "Display None Button")
check_button_visibility("offscreenButton", "Offscreen Button")

driver.quit()