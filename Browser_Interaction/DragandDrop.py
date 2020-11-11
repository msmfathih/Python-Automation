from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(10)
driver.maximize_window()


"""Handling multiple actions"""
"""click and hold, move to element,drop the element"""

source_element = driver.find_element_by_xpath("//div[@id='box6']")
target_element = driver.find_element_by_xpath("//div[@id='box106']")
ack_chains = ActionChains(driver)

ack_chains.click_and_hold(source_element)\
    .move_to_element(target_element)\
    .release()\
    .perform()


source_element = driver.find_element_by_xpath("//div[@id='box5']")
target_element = driver.find_element_by_xpath("//div[@id='box105']")
action_chains = ActionChains(driver)

action_chains.click_and_hold(source_element)\
    .move_to_element(target_element)\
    .release()\
    .perform()

"""Single Action drag and drop"""
# ack = ActionChains(driver)
# ack.click().perform()


# source_element = driver.find_element_by_xpath("//div[@id='box6']")
# target_element = driver.find_element_by_xpath("//div[@id='box106']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
# source_element = driver.find_element_by_xpath("//div[@id='box5']")
# target_element = driver.find_element_by_xpath("//div[@id='box105']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
# source_element = driver.find_element_by_xpath("//div[@id='box3']")
# target_element = driver.find_element_by_xpath("//div[@id='box103']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
# source_element = driver.find_element_by_xpath("//div[@id='box7']")
# target_element = driver.find_element_by_xpath("//div[@id='box107']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
# source_element = driver.find_element_by_xpath("//div[@id='box7']")
# target_element = driver.find_element_by_xpath("//div[@id='box107']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
#
# source_element = driver.find_element_by_xpath("//div[@id='box4']")
# target_element = driver.find_element_by_xpath("//div[@id='box104']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
#
# source_element = driver.find_element_by_xpath("//div[@id='box1']")
# target_element = driver.find_element_by_xpath("//div[@id='box101']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
#
#
# source_element = driver.find_element_by_xpath("//div[@id='box2']")
# target_element = driver.find_element_by_xpath("//div[@id='box102']")
# action = ActionChains(driver)
# action.drag_and_drop(source_element,target_element).perform()
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
