from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TestSuiteDemo3(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()
        cls.driver.get("http://demo.automationtesting.in/Register.html")
        print("Title of the page is " + cls.driver.title)
        time.sleep(2)


    def test_priority10_mouseHover(self):
        driver = self.driver
        self.ack = ActionChains(driver)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Interactions')]")).perform()
        time.sleep(2)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Drag and Drop')]")).perform()
        time.sleep(3)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Static')]")).click().perform()
        time.sleep(3)
        driver.quit()



    @classmethod
    def tearDownClass(cls) -> None:
        # self.driver.quite()
        print("Test has completed")

if __name__ == '__main__':
    unittest.main(verbosity=2)

