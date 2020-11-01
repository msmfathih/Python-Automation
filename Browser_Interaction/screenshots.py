from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/?gl=us&hl=en&pws=0")
driver.implicitly_wait(10)

driver.save_screenshot("E:\DevOps\homepage.png")

driver.get_screenshot_as_file("E:\DevOps\homepage.png")