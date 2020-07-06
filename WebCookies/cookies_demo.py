from selenium import webdriver


driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
driver.get("https://www.amazon.ae/")

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#adding new cookie cookie=dictionary
cookie = {'name':'MyCookie','value=':'1234567890'}
driver.add_cookie(cookie)
driver.delete_cookie(cookie)


#printing new cookie
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


