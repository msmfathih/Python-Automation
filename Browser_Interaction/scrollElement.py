from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.implicitly_wait(10)

#scroll down by pixel
driver.execute_script("window.scrollBy(0,2000)","")

#scroll down till element visible
flag = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div/div[164]/div/a/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)

#scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")




