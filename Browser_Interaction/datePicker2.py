from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
baseURL = "https://www.goibibo.com/"
driver.implicitly_wait(10)
driver.get(baseURL)

click_datapicker = driver.find_element(By.XPATH, "//input[contains(@id,'departure')]")
click_datapicker.click(),time.sleep(2)

driver.find_element(By.XPATH, "//div[text()='30']").click()

alldates = driver.find_elements(By.ID, "//div[@class='DayPicker-Body']//div[@class='calDate']")
for dateelement in alldates:
    date = dateelement.text
    print(date)
    if date == '30':
        dateelement.click()
        break









