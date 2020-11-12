from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


def setUp():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    print("Maximized browser")

def test_actions():
    driver.get("http://demo.automationtesting.in/")

    driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
    time.sleep(2)

    driver.find_element_by_id("enterimg").click()
    time.sleep(2)


def test_teardown():
    driver.quite()
    driver.close()
    print("Test has completed")


