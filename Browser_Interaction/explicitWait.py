from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class explicitWait():
    def waitTest(self):
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        baseURL = "https://www.expedia.com/"
        driver.get(baseURL)

        clickOnFlightLink = driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']//span[@class='icons-container']")
        clickOnFlightLink.click()

        enterFromAirport = driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
        enterFromAirport.send_keys("auh")
        time.sleep(2)

        enterToAirport = driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
        enterToAirport.send_keys("lhr")
        time.sleep(2)

        driver.find_element_by_xpath("//input[@id='flight-departing-single-hp-flight']").send_keys("07/09/2020")
        time.sleep(2)
        driver.find_element_by_id("gcw-flights-form-hp-flight")
        time.sleep(5)

        #explicit wait condition
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        time.sleep(2)
        driver.quit()


main_class=explicitWait()
main_class.waitTest()




