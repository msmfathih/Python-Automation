from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="OKTab"]/button').click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept() #click on ok and accept it


# driver.find_element(By.XPATH, "//a[contains(text(),'Alert with OK & Cancel')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.dismiss() #dismiss the alert


# driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="Textbox"]/button').click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("Hi world")
# time.sleep(2)
# alert.accept()
