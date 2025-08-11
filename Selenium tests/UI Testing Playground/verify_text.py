from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://uitestingplayground.com/verifytext"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

# normalize-space(.) will only grab the current element
# normalize-space() will grab the element along with its children
# in this case, the child is another span element that 
# can be accessed with an additional /span
text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(normalize-space(), 'Welcome')]"))
)
# Should print(Welcome...)
print(text.text)

driver.quit()