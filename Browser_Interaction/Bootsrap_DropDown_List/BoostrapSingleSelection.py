from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)


driver.find_element(By.ID, 'msdd').click()
time.sleep(3)
drop_list = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all') #get the specific element's class
time.sleep(3)

for ele in drop_list:
    print(ele.text)
    if ele.text == 'Dutch':
        ele.click()
        break




