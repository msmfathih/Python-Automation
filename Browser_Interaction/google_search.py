from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/?gl=us&hl=en&pws=0")
driver.implicitly_wait(10)

driver.find_element(By.NAME, 'q').send_keys("Amazon ae")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'amazon ae':
        ele.click()
        break

time.sleep(10)
driver.quit()

