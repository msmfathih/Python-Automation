from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)


def select_country(self):
    self.driver.find_element(By.XPATH, "//*[@class='select2-selection select2-selection--single']").click()
    time.sleep(2)
    drop_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.select2-selection__rendered')

    time.sleep(2)

    for ele in drop_list:
        print(ele.text)
        if ele.text == "India":
            ele.click()
            break




