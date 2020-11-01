from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
print("Title of the page is " + driver.title)
assert "Register" in driver.title

ack = ActionChains(driver)
# ack.click().perform()
# ack.context_click().perform() #right click

ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Interactions')]")).perform()
print("Clicked on interaction page")
time.sleep(2)
ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Drag and Drop')]")).perform()
print("Clicked on drag and drop page")
time.sleep(2)
ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Static')]")).click().perform()
print("Clicked on static page")

driver.quit()
