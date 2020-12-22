from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--lang=en-GB")
#driver = webdriver.Chrome(executable_path=r"D:\Chrome_Driver\chromedriver.exe", chrome_options=options)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.implicitly_wait(10)
driver.maximize_window()


input_search = driver.find_element_by_name("q")
input_search.send_keys("Selenium")
wait = WebDriverWait(driver, 10, poll_frequency=3, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
btn_search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")))
btn_search.click()

#poll frequency= how many times browser should repeat and looking for that condition(element visible)
#ignored_exceptions = ability to ignore some errors when they occurs and wait for the element visible

