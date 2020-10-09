from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class TestExecution():
    @pytest.mark.run(order=1)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(5)
        # driver.maximize_window()
        print("Maximized browser")

    @pytest.mark.run(order=2)
    def test_actions(self):
        driver.get("http://demo.automationtesting.in/")

        driver.find_element_by_id("email").send_keys("admin@gmail.com")
        time.sleep(2)

        driver.find_element_by_id("enterimg").click()
        time.sleep(2)

    @pytest.mark.run(order=3)
    def test_enterForm(self):
        firstName = driver.find_element_by_xpath("//input[@placeholder='First Name']")
        firstName.send_keys("fathih")

        lastName = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
        lastName.send_keys("mohamed")
        time.sleep(2)

        enterAddress = driver.find_element_by_xpath(
            "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']")
        enterAddress.send_keys("UAE Abu Dhabi")
        time.sleep(2)

        enterEmail = driver.find_element_by_xpath(
            "//input[@class='form-control ng-pristine ng-untouched ng-valid-email ng-invalid ng-invalid-required']")
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPhoneNumber = driver.find_element_by_xpath(
            "//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required ng-valid-pattern']")
        enterPhoneNumber.send_keys("052854272")


    @pytest.mark.run(order=4)
    def test_radiobutton(self):
        clickRadioBtn = driver.find_element_by_xpath("//label[1]//input[1]")
        clickRadioBtn.click()
        time.sleep(2)
        clickRadioBtn1 = driver.find_element_by_xpath("//label[2]//input[1]")
        clickRadioBtn1.click()


    @pytest.mark.run(order=5)
    def test_check_boxes(self):
        clickCheckBox = driver.find_element_by_id("checkbox1")
        clickCheckBox.click()
        time.sleep(2)

        clickCheckBox = driver.find_element_by_id("checkbox2")
        clickCheckBox.click()
        time.sleep(2)

    @pytest.mark.run(order=6)
    def test_select_language(self):
        driver.find_element(By.ID, 'msdd').click()
        time.sleep(3)
        drop_list = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')  # get the specific element's class
        time.sleep(3)

        for ele in drop_list:
            print(ele.text)
            if ele.text == 'Dutch':
                ele.click()
                break

    @pytest.mark.run(order=7)
    def test_uploadFile(self):
        uploadFile = driver.find_element_by_id("imagesrc")
        uploadFile.send_keys("C://Users//fathih//PycharmProjects//Python Automation//Image//python.png")
        time.sleep(5)
        # driver.close()


    def test_teardown(self):
        #driver.quite()
        print("Test has completed")





