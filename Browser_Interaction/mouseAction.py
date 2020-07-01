from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome

driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
print("Title of the page is " + driver.title)
assert "Register" in driver.title

ack = ActionChains(driver)
# ack.click().perform()
# ack.context_click().perform() #right click

ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Interactions')]")).perform()
time.sleep(2)
ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Drag and Drop')]")).perform()
time.sleep(2)
ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Static')]")).click().perform()

driver.quit();