from environment import *
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException


# BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
# BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
# desired_cap = {
#    'os_version': '10',
#    'resolution': '1920x1080',
#    'browser': 'Chrome',
#    'browser_version': '94.0',
#    'os': 'Windows',
#    'name': 'BStack-[Python] Smoke Test for shadowandact.com google search for shadow & act on desktop',
#    'build': 'BStack Build Number'
# }
#
# desired_cap["chromeOptions"] = {}
# desired_cap["chromeOptions"]["args"] = ["--disable-notifications"]
# driver = webdriver.Remote(
#     command_executor='https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)


def navigate_to_google_page():
    driver.maximize_window()
    # driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(2)
    print(driver.title)


def search_keyword(website_name):
    print("function called search_keyword")
    search_text_box = driver.find_element(By.XPATH, "//input[@title='Search']")
    search_text_box.send_keys(website_name)
    search_text_box.send_keys(Keys.RETURN)
    time.sleep(2)


def launch_app():
    print("function called launch_app")
    result = driver.find_element(By.XPATH, "//a[@href='https://shadowandact.com/']")
    result.click()
    time.sleep(5)
