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

driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
driver.find_element(By.CLASS_NAME, "ladda-label").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Barang']").click()
driver.find_element(By.XPATH, "//span[text()='Katalog']").click()
driver.find_element(By.XPATH, "//span[text()='Master']").click()
time.sleep(3)
driver.find_element(
    By.XPATH, "//button[@class='ladda-button btn btn-primary m-l-xs']"
).click()
driver.find_element(By.NAME, "item_group_name").send_keys("Milo")
# time.sleep(3)
driver.find_element(By.CLASS_NAME, "selectivity-input").click()
# time.sleep(3)

sel1 = driver.find_element(By.CLASS_NAME, "selectivity-search-input")
sel1.send_keys("Makan" + Keys.RETURN)
time.sleep(3)
sel1.send_keys(Keys.RETURN)

driver.find_element(By.NAME, "brand_name").send_keys("Milo")

driver.find_element(By.NAME, "item_code").send_keys("P0003")

driver.find_element(By.NAME, "barcode").send_keys("33234567890")

driver.find_element(
    By.CSS_SELECTOR,
    "div.RichTextEditor__block___2Vs_D.RichTextEditor__paragraph___3NTf9",
).send_keys(
    "lorem ipusm sit amet kemana ada memasuk apapun bentuknya laser kebudayan bende alah"
)
time.sleep(3)
driver.find_element(By.CLASS_NAME, "rug-file-input").send_keys(
    "Macintosh HD/Users/abd.rauf/Downloads/6.png"
)
