from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

options = webdriver.ChromeOptions()
# change this to True
options.headless = False
# options.headless = True
# options.add_argument('--no-sandbox')
options.add_argument("--disable-notifications")
options.add_argument('--start-maximized')
# options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

user_agent = \
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 PTST/1.0'
options.add_argument('user-agent={0}'.format(user_agent))
# use this code below to execute headless state
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install()) for blavity deployment
# for desktop execution
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# for linux debian
# tried this getting error as "The process started from chrome location /usr/bin/chromium is no longer running,
# so ChromeDriver is assuming that Chrome has crashed.)"
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)

# for linux debian working on debian 10 linux.
# driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

url_name = "https://staging.shadowandact.com/"


def environment():
    driver.maximize_window()
    driver.get(url_name)
    time.sleep(5)
    print(driver.title)


def page_load():
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
    assert driver.current_url == url_name, "url does not match"


def post_page_load_pop_up():
    # try:
    #     event_promo_pop_up = driver.find_element_by_xpath(
    #       "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
    #     driver.execute_script("arguments[0].click();", event_promo_pop_up)
    # except NoSuchElementException:
    #     print("event promo pop-up does not exist")
    # try:
    #     driver.switch_to.frame("sp_message_iframe_565136")
    #     pop_up_text = driver.find_element(By.XPATH, "//p[normalize-space()='We value your privacy']")
    #     if pop_up_text.is_displayed():
    #         accept_button = driver.find_element(By.XPATH, "//button[@title='Accept']")
    #         accept_button.click()
    #     driver.switch_to.parent_frame()
    # except NoSuchElementException:
    #     print("blavity news privacy pop-up does not exist")
    footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
    driver.execute_script("arguments[0].click();", footer_xpath)
    assert driver.title == "SHADOW & ACT", "title does not match"
