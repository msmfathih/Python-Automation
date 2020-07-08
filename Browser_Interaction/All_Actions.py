from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest


driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")

class clickSendKeys():
    def actions(self,driver):
        baseUrl = "https://letskodeit.teachable.com/"
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()


        loginlink = driver.find_element(By.XPATH, "//a[@class='fedora-navbar-link navbar-link']")
        loginlink.click()
        time.sleep(2)

        verifyPageName = driver.find_element(By.XPATH, "//h1[contains(text(),'Practice Page')]")
        if verifyPageName is not None:
            print("Verified Page Name")
        else:
            print("Page name is not verified")

        time.sleep(2)
        enterName = driver.find_element(By.XPATH, "//input[@id='name']")
        enterName.send_keys("test23")

        time.sleep(2)
        enterName.clear()

        time.sleep(2)
        enterName2 = driver.find_element(By.XPATH, "//input[@id='name']")
        enterName2.send_keys("test45")

        driver.back()
        time.sleep(2)


    def isEnabledd(self,driver):

        loginlink2 = driver.find_element(By.XPATH, "//a[@class='fedora-navbar-link navbar-link']")
        loginlink2.click()
        time.sleep(2)

        title = driver.title
        print("title of the page is " + title)
        time.sleep(2)

        practiceBtnEnabled = driver.find_element(By.XPATH, "//a[@class='fedora-navbar-link navbar-link']")
        practiceBtnEnabled.is_enabled()
        print("Practice button link is enabled")
        time.sleep(2)


    def selectRadioBtn_CheckBox(self):

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()
        print("benz radio button is selected.? "+ str(benzRadioBtn.is_selected()))
        time.sleep(1)

        bmwCheckBox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckBox.click()
        print("bmw check box is selected..?" + str(bmwCheckBox.is_selected()))
        time.sleep(1)

        benzCheckBox = driver.find_element(By.ID, "benzcheck")
        benzCheckBox.click()
        print("benz check box is selected..?" + str(benzCheckBox.is_selected()))
        time.sleep(1)


    def findListofElement(self):

        radioBtnList = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioBtnList)
        print("Size of the radio button is "+ str(radioBtnList))

        for radioButton in radioBtnList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(1)



    def selectDropDown(self):

        element1 = driver.find_element_by_id("carselect")
        sel = Select(element1)
        sel.select_by_value("benz")
        time.sleep(1)

        element2 = driver.find_element_by_id("carselect")
        sel=Select(element2)
        sel.select_by_index(0)
        time.sleep(1)

        element3 = driver.find_element_by_id("carselect")
        sel=Select(element3)
        sel.select_by_visible_text("Honda")
        time.sleep(1)


    def showhideElement(self):

        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible "+ str(textBoxState))
        time.sleep(2)

        driver.find_element_by_id("hide-textbox").click()
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible " + str(textBoxState))
        time.sleep(2)

        driver.find_element_by_id("show-textbox").click()
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible " + str(textBoxState))


    def getText(self):

        openTabElement = driver.find_element_by_id("opentab")
        elementText = openTabElement.text
        print("Text on element is " + elementText)
        time.sleep(2)

    def getAttribute(self):

        element = driver.find_element_by_id("name")
        # result = element.get_attribute("class")
        result = element.get_attribute("type")

        print("Value of the attribute is: "+ result)
        time.sleep(2)
        driver.forward()


    def dynamicXpath(self):

        driver.get("https://letskodeit.teachable.com/courses/")

        #search courses
        searchBox = driver.find_element_by_id("search-courses")
        searchBox.send_keys("learn python")

        #select course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("Learn Python 3 from scratch")
        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(2)
        driver.quit()






main_class=clickSendKeys()
main_class.actions(driver)
main_class.isEnabledd(driver)
main_class.selectRadioBtn_CheckBox()

main_class.findListofElement()
main_class.selectDropDown()
main_class.showhideElement()


main_class.getText()
main_class.getAttribute()
main_class.dynamicXpath()
