from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TestSuiteDemo4(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demo.automationtesting.in/Register.html")

    def test_priority11_getalert(self):
        driver = self.driver
        self.ack = ActionChains(driver)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'SwitchTo')]")).perform()
        time.sleep(2)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Alerts')]")).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='btn btn-danger']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        # self.driver.quite()
        print("Test has completed"
  )

if __name__ == '__main__':
        unittest.main(verbosity=2)