from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

email =""

for x in range(1,5):
    email="ashika"+str(x)+"@gmail.com"
    driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
    driver.get("http://rentvehicles.multicompetition.com/login")
    driver.implicitly_wait(5)

    enterEmail = driver.find_element(By.ID, 'email')
    enterEmail.send_keys(email)
    time.sleep(2)

    # enterPassword = driver.find_element(By.ID, 'password')
    # enterPassword.send_keys("admin@123")
    #
    # enterLoginBtn = driver.find_element_by_id("btnLogin")
    # enterLoginBtn.click()
    #
    # driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
    # time.sleep(2)
    #
    # # driver.find_element_by_xpath("//button[@id='submitBtn']").click()
    # # driver.find_element_by_id("submitBtn").click()
    #
    # element = driver.find_element_by_id("submitBtn")
    # driver.execute_script("arguments[0].click();", element)
    driver.close()




