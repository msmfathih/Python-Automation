from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
import time
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


"""Method 1"""
# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

"""Method 2"""
desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)

driver.implicitly_wait(10)

driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME, 'h1').text)


