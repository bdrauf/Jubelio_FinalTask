from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.maximize_window()
driver.get("https://app.jubelio.com/login")
time.sleep(3)

driver.find_element(By.NAME, "email").send_keys("InvalidEmail")
driver.find_element(By.NAME, "password").send_keys("invalidpassword")
driver.find_element(By.CLASS_NAME, "ladda-label").click()
