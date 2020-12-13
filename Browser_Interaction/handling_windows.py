from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
baseURL = "http://demo.automationtesting.in/Windows.html"
driver.get(baseURL)


driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)  #parent window handlevalue

handles = driver.window_handles  # returns all the handle of opened windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":  # parant window only close
        driver.close()

# driver.close()


