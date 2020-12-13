from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class UnitTestExample(unittest.TestCase):

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


    def test_priority6_selectCountry(self):
        selectCountry = self.driver.find_element_by_xpath("//span[@class='select2-selection select2-selection--single']")
        selectCountry.send_keys("Australia")
        time.sleep(2)
        # self.driver.find_element_by_id("msdd").send_keys("Arabic")
        # time.sleep(2)


    def test_priority7_perform_skills(self):
        #self.driver.find_elements_by_id("Skills").send_Keys("Andriod")
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
        #self.driver.find_element_by_id("yearbox").send_keys("2010")

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


        # for values in dropOptionList:
        #     print (values.text.encode('ascii','ignore').decode('ascii'))

        # allLinks = self.driver.find_elements_by_tag_name("a")
        # print("The length of the list is", len(allLinks))
        #
        # for values in allLinks:
        #     print (values.get_attribute("href"))
        #     time.sleep(2)
    #
    def test_priority10_mouseHover(self):

        driver = self.driver
        self.ack = ActionChains(driver)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Interactions')]")).perform()
        time.sleep(2)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Drag and Drop')]")).perform()
        time.sleep(2)
        self.ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Static')]")).click().perform()


        # 1.navigate by pixel
        # driver.execute_script("window.scrollBy(0,1000)","")
        #
        # 2.Scroll down the page till the element is visible
        # flag = driver.find_element_by_xpath("indian flag xpath")
        # driver.execute_script("argument[0].scrollIntoView();",flag)

        #3.scrool down the page till the end of the page
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quite()
        print("Test has completed")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/fathih/PycharmProjects/Python Automation/Report'))
