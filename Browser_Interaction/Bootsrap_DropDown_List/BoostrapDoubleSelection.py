from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)


def select_values(options_list, value):
    if not value[0] == 'all':
        for ele in drop_list:
            print(ele.text)
            for k in range(len(value)):  # calling multiple values
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        for ele in options_list:
            ele.click()


driver.find_element(By.ID, 'msdd').click()
time.sleep(3)
drop_list = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')

value_list = ['all']
select_values(drop_list,value_list)



