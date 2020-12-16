from selenium import webdriver
import time
import openpyxl
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
    myphone.append(phone.text)

print("*"*50)

for price in phone_price:
    myprice.append(price.text)


final_list = zip(myphone,myprice)
print("Part 1")


wb = Workbook
sh1 = wb.active

for x in list(final_list):
    sh1.append(x)

wb.save("FinalRecords.xlsx")
print("Part 2")



driver.quit()

