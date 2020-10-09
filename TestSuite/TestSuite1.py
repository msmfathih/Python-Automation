from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TestSuiteDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_priority1_actions(self):
        self.driver.get("http://demo.automationtesting.in/")
        print("Title of the page is " + self.driver.title)
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
        time.sleep(2)

        self.driver.find_element_by_id("enterimg").click()
        time.sleep(2)


    def test_priority2_enterForm(self):
        firstName = self.driver.find_element_by_xpath("//input[@placeholder='First Name']")
        firstName.send_keys("fathih")

        lastName = self.driver.find_element_by_xpath("//input[@placeholder='Last Name']")
        lastName.send_keys("mohamed")
        time.sleep(2)

        enterAddress = self.driver.find_element_by_xpath(
            "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']")
        enterAddress.send_keys("UAE Abu Dhabi")
        time.sleep(2)

        enterEmail = self.driver.find_element_by_xpath(
            "//input[@class='form-control ng-pristine ng-untouched ng-valid-email ng-invalid ng-invalid-required']")
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPhoneNumber = self.driver.find_element_by_xpath(
            "//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required ng-valid-pattern']")
        enterPhoneNumber.send_keys("052854272")

    def test_priority3_uploadFile(self):
        uploadFile = self.driver.find_element_by_id("imagesrc")
        uploadFile.send_keys("C://Users//fathih//PycharmProjects//Python Automation//Image//python.png")
        time.sleep(5)

    def test_priority4_perform_radio_button(self):
        clickRadioBtn = self.driver.find_element_by_xpath("//label[1]//input[1]")
        clickRadioBtn.click()
        time.sleep(2)
        clickRadioBtn1 = self.driver.find_element_by_xpath("//label[2]//input[1]")
        clickRadioBtn1.click()


    def test_priority5_perform_check_boxes(self):
        clickCheckBox = self.driver.find_element_by_id("checkbox1")
        clickCheckBox.click()
        time.sleep(2)

        clickCheckBox = self.driver.find_element_by_id("checkbox2")
        clickCheckBox.click()
        time.sleep(2)
        self.driver.quit()



    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quite()
        print("Test has completed")



if __name__ == '__main__':
    unittest.main(verbosity=2)
