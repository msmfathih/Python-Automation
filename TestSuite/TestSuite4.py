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

    def test_priority11_get_alert(self):
        driver = self.driver
        self.ack = ActionChains(driver)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'SwitchTo')]")).perform()
        time.sleep(2)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Alerts')]")).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='btn btn-danger']").click()
        time.sleep(5)
        driver.switch_to.alert.accept()

    #cancel alert message
    def test_priority12_get_alert_cancel(self):
        driver = self.driver
        self.driver.find_element_by_xpath("//a[contains(text(),'Alert with OK & Cancel')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

    #enter text in laert box
    def test_priority13_get_alert_textbox(self):
        driver = self.driver
        self.driver.find_element_by_xpath("//a[contains(text(),'Alert with Textbox')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        # driver.switch_to.alert.send_keys("fathih")
        driver.quit()



    @classmethod
    def tearDownClass(cls) -> None:
        # self.driver.quite()
        print("Test has completed")

if __name__ == '__main__':
        unittest.main(verbosity=2)