from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class ListOfElements():
    def testMethod(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Clss name ->Size of the list is: "+ str(length))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "tr")
        length1 = len(elementListByTagName)

        if elementListByClassName is not None:
            print("Tag name ->Size of the list is: " + str(length1))


cc = ListOfElements()
cc.testMethod()