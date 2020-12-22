from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.ae/")
driver.implicitly_wait(10)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Samsung Phones")
driver.find_element(By.XPATH, "//*[@id='nav-search-submit-text']/input").click()

driver.find_element(By.XPATH, "//span[text()='SAMSUNG']").click()

phone_names = driver.find_elements(By.XPATH, "//span[contains(@class, 'a-size-base-plus a-color-base a-text-normal')]")

phone_price = driver.find_elements(By.XPATH, "//span[contains(@class, 'price-whole')]")

myphone=[]
myprice=[]

for phone in phone_names:
    print(phone.text)
    myphone.append(phone.text)

print("*"*50)

for price in phone_price:
    print(price.text)
    myprice.append(price.text)

final_list = zip(myphone,myprice)

for data in list(final_list):
    print(data)




driver.quit()

