from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome

driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)
driver.maximize_window()


"""
Types of Alert 
"""
#
# ack = ActionChains(driver)
# ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'SwitchTo')]")).perform()
# time.sleep(2)
# ack.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'Alerts')]")).click().perform()
# time.sleep(5)
# driver.find_element_by_xpath("//button[@class='btn btn-danger']").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)
#
# driver.find_element_by_xpath("//a[contains(text(),'Alert with OK & Cancel')]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
# time.sleep(3)
# driver.switch_to.alert.dismiss()
# time.sleep(3)
#
#
# driver.find_element_by_xpath("//a[contains(text(),'Alert with Textbox')]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
# time.sleep(3)
# driver.switch_to.alert.accept()
# driver.switch_to.alert.send_keys("fathih")

"""
-------------------**********************------------------------
"""

"""
Handling the drag and drop
"""

ack = ActionChains(driver)
ack.click().perform()

source_element = driver.find_element_by_xpath("//div[@id='box6']")
target_element = driver.find_element_by_xpath("//div[@id='box106']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()

source_element = driver.find_element_by_xpath("//div[@id='box5']")
target_element = driver.find_element_by_xpath("//div[@id='box105']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()

source_element = driver.find_element_by_xpath("//div[@id='box3']")
target_element = driver.find_element_by_xpath("//div[@id='box103']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()

source_element = driver.find_element_by_xpath("//div[@id='box7']")
target_element = driver.find_element_by_xpath("//div[@id='box107']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()

source_element = driver.find_element_by_xpath("//div[@id='box7']")
target_element = driver.find_element_by_xpath("//div[@id='box107']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()


source_element = driver.find_element_by_xpath("//div[@id='box4']")
target_element = driver.find_element_by_xpath("//div[@id='box104']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()


source_element = driver.find_element_by_xpath("//div[@id='box1']")
target_element = driver.find_element_by_xpath("//div[@id='box101']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()


source_element = driver.find_element_by_xpath("//div[@id='box2']")
target_element = driver.find_element_by_xpath("//div[@id='box102']")
action = ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
