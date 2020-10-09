from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class browserNavigates():
    def actions(self):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.get(baseUrl)

        driver.maximize_window()


        title = driver.title
        print("title of the page is "+ title)

        currentUrl = driver.current_url
        print("Current URL of the page is "+currentUrl)

        driver.refresh()
        print("Browser refreshed 1st time")

        driver.get(currentUrl)
        print("Browser Refreshed 2nd time")

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        driver.back()
        print("One step back")
        driver.forward()
        print("One step forward")

        pageSource = driver.page_source
        print(pageSource)




aa=browserNavigates()
aa.actions()