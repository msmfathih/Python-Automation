from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pip._vendor.distlib import resources
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
timeout = 10

try:
    element_present = EC.presence_of_element_located((By.LINK_TEXT, 'Sitemap'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out while waiting for page to load")
driver.quit()