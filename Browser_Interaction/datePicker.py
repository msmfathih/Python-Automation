from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
baseURL = "http://demo.automationtesting.in/Datepicker.html"
driver.get(baseURL)


click_datapicker = driver.find_element(By.ID, 'datepicker1')
click_datapicker.click(),time.sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

pick_date = driver.find_element(By.XPATH, "//a[contains(text(),'22')]")
pick_date.click()


driver.find_element(By.CSS_SELECTOR, "#datepicker2").send_keys("11/26/2020")





