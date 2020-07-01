from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class RunFFTests():
    def testMethod(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        #driver = webdriver.Firefox(executable_path="E:\\Automation\\Webdrivers\\geckodriver\\geckodriver.exe")
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.get(baseUrl)

        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("We found on element")

        elementByName = driver.find_element_by_name("enter-name")
        if elementById is not None:
            print("We found on element")

        elementByCss = driver.find_element_by_css_selector("#alertbtn")
        if elementByCss is not None:
            print("We found on element: Css selector")

        elementByLinkedText = driver.find_element_by_link_text("Login")
        if elementByCss is not None:
            print("We found on element: LinkedText")

        elementByParcialLink = driver.find_element_by_partial_link_text("Practi")
        if elementByCss is not None:
            print("We found on element: Parcial LinkedText")

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("testing")


        time.sleep(5)


ff = RunFFTests()
ff.testMethod()