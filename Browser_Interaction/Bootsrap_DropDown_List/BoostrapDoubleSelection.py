from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class TestValue():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("http://demo.automationtesting.in/Register.html")
    driver.implicitly_wait(10)

    def select_values(drop_list, value):
        for ele in drop_list:
            print(ele.text)
            for k in range(len(value)):  # calling multiple values
                if ele.text == value[k]:
                    ele.click()
                    break

            if ele.text == value:  # calling multiple values
                ele.click()
                break

    driver.find_element(By.ID, 'msdd').click()
    time.sleep(3)
    drop_list = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')

    value_list = ['Arabic', 'English', 'Dutch', 'French', 'German']
    select_values(drop_list, value_list)





