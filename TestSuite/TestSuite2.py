from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TestSuiteDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()
        cls.driver.get("http://demo.automationtesting.in/Register.html")
        print("Title of the page is " + cls.driver.title)
        # time.sleep(2)
        # cls.driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
        # time.sleep(2)
        #
        # cls.driver.find_element_by_id("enterimg").click()
        time.sleep(2)


    def test_priority6_selectCountry(self):
        selectCountry = self.driver.find_element_by_xpath("//span[@class='select2-selection select2-selection--single']")
        selectCountry.send_keys("Australia")
        time.sleep(2)


    def test_priority7_perform_skills(self):
        # self.driver.find_elements_by_id("Skills").send_Keys("Andriod")
        skillsDropDown = self.driver.find_element_by_id("Skills")
        select = Select(skillsDropDown)
        select.select_by_visible_text("Android")
        time.sleep(2)

    def test_priority8_select_country(self):
        selectCountry = self.driver.find_element_by_id("countries")
        select = Select(selectCountry)
        select.select_by_visible_text("Australia")
        time.sleep(2)

    def test_priority9_select_DOB(self):
        # self.driver.find_element_by_id("yearbox").send_keys("2010")

        dropDownYear = self.driver.find_element_by_id("yearbox")
        select = Select(dropDownYear)
        select.select_by_value("2010")
        time.sleep(2)

        dropDownMonth = self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        select = Select(dropDownMonth)
        select.select_by_index(5)

        dropDownDay = self.driver.find_element_by_id("daybox")
        select = Select(dropDownDay)
        select.select_by_index(11)
        time.sleep(2)

        dropOptionList = self.driver.find_elements_by_tag_name("option")
        print("The length of the list is", len(dropOptionList))
        self.driver.quit()


    @classmethod
    def tearDownClass(cls) -> None:
        # self.driver.quite()
        print("Test has completed")

if __name__ == '__main__':
    unittest.main(verbosity=2)

