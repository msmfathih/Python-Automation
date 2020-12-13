from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://rentvehicles.multicompetition.com/")
driver.implicitly_wait(10)

enterEmail = driver.find_element(By.ID, 'email')
enterPassword = driver.find_element(By.ID, 'password')
enterLoginBtn = driver.find_element_by_id("btnLogin")

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(enterEmail, 'admin@gmail.com').perform()
act_chains.send_keys_to_element(enterPassword, 'admin@123').perform()
act_chains.click(enterLoginBtn).perform()





