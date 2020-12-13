from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://rentvehicles.multicompetition.com/login")
enterEmail = driver.find_element(By.ID, 'email')
enterEmail.send_keys("admin@gmail.com")
time.sleep(2)

enterPassword = driver.find_element(By.ID, 'password')
enterPassword.send_keys("admin@123")

enterLoginBtn = driver.find_element_by_id("btnLogin")
enterLoginBtn.click()
time.sleep(3)


links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present:", len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT, 'Vehicles').click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'Vehicle Owners').click()

