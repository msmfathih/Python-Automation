from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
baseURL = "https://www.google.lk/maps/@24.4444901,54.370247,13z"
driver.get(baseURL)
driver.implicitly_wait(10)
# driver.maximize_window()
time.sleep(3)


def search_location():
    search_location = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
    search_location.send_keys("Dubai"),time.sleep(2)

    click_location = driver.find_element_by_xpath("//button[@id='searchbox-searchbutton']")
    click_location.click(), time.sleep(2)

search_location()


def directions():
    direction = driver.find_element(By.XPATH, "//body/jsl[1]/div[3]/div[9]/div[7]/div[1]/d"
                                              "iv[1]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]")
    direction.click()

directions()

def find():
    start_location = driver.find_element(By.XPATH, '//body/jsl[1]/div[3]/div[9]/div[3]/'
                                                   'div[1]/div[2]/div[1]/div[3]/div[1]/div[1]'
                                                   '/div[2]/div[1]/div[1]/input[1]')
    start_location.send_keys("Dubai")

    end_location = driver.find_element(By.XPATH, '//body/jsl[1]/div[3]/div[9]/div[3]/div[1]/div[2]/div'
                                                 '[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]')
    end_location.send_keys("Abu dhabi"),time.sleep(2)

    search_location = driver.find_element(By.XPATH, "/html/body/jsl/div[3]/div[9]/div["
                                                    "3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]")
    search_location.click()


find()






#
# click_on_language = driver.find_element(By.XPATH, "//*[@id='settings']/div/div[2]/div/ul[2]/li[2]/button/span")
# click_on_language.click(),time.sleep(2)
#
# select_english = driver.find_element(By.XPATH, "//*[@id='languages']/div/div[2]/div[2]/ul[1]/li[11]/span")
# select_english.click()

# element = driver.find_element_by_xpath("//*[@id='languages']/div/div[2]/div[2]/ul[1]/li[11]/span")
# driver.execute_script("arguments[0].click();", element)

