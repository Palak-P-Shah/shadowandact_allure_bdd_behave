import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


url_shadowandact = "https://staging.shadowandact.com/"
BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
desired_cap = {
  'os_version': '10.0',
  'device': 'Google Pixel 3',
  'real_mobile': 'true',
  'browserstack.local': 'false',
  'browserName': 'Chrome',
  'browser_version': 'latest',
  'os': 'Android',
  'name': 'BStack-[Python] Smoke Test for staging.shadowandact.com of film page is as expected on android phone chrome browser',
  'build': 'BStack Build Number'
}

desired_cap["chromeOptions"] = {}
desired_cap["chromeOptions"]["args"] = ["--disable-notifications"]
driver = webdriver.Remote(
    command_executor='https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)


def environment():
    driver.get(url_shadowandact)
    time.sleep(5)
    print(driver.title)


def page_load():
    try:
        WebDriverWait(driver, 20).until(ec.title_is("SHADOW & ACT"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": for staging.shadowandact.com, for android '
          'chrome, took too long but no response, checking title"}}')
        driver.quit()


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


def verify_particular_page(page):
    temp_variable = ''
    print("value passed is :- ", page)
    if page == 'FILM':
        temp_variable = 'Film'
    elif page == 'TELEVISION':
        temp_variable = 'Television'
    elif page == 'WEB SERIES':
        temp_variable = 'Web Series'
    elif page == 'INTERVIEWS':
        temp_variable = 'Interviews'
    print("inside function verify particular page")
    btn = driver.find_element(
      By.XPATH,
      "(//button[@class='navbar-toggler bg-transparent border-0 d-desktop-none text-center text-white'])[1]")
    btn.click()
    var_link = driver.find_element(By.XPATH, "//a[normalize-space()='" + page + "']")
    assert var_link.is_displayed(), temp_variable + " link is not displayed in the navigation bar"
    var_link.click()
    title = temp_variable + " - SHADOW & ACT"
    print(title)
    WebDriverWait(driver, 40).until(ec.title_is(title))
    assert driver.title == temp_variable + " - SHADOW & ACT", "title of the page " + page + " does not match"
    page_header = driver.find_element(By.XPATH, "//h1[normalize-space()='" + temp_variable + "']")
    assert page_header.is_displayed(), "header of the page " + temp_variable + " is not displayed"
    verify_each_article(page, temp_variable)
    verify_number_of_articles(temp_variable)
    verify_final_article(page, temp_variable)
    verify_footer_exists(page)


def verify_footer_exists(page):
    print("in function verify_footer_exists")
    temp_footer = driver.find_element(By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    actions = ActionChains(driver)
    actions.move_to_element(temp_footer).perform()
    assert temp_footer.is_displayed(), "footer is not present for ShadowAndAct page :" + page


def verify_number_of_articles(temp_variable):
    print("inside function verify_number_of_articles")
    temp_number = driver.find_elements(By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles are :- ", len(temp_number))
    assert len(temp_number) > 0, "Articles are not present for " + temp_variable + " page"
    load_more_stories_button = driver.find_element(By.XPATH, "//button[normalize-space()='Load More Stories']")
    load_more_stories_button.click()
    time.sleep(2)
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='Load More Stories']")))
    temp_number_post_click = driver.find_elements(
      By.XPATH,
      "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles after 'Load More Stories' button click are :- ", len(temp_number_post_click))
    assert len(temp_number_post_click) > len(temp_number), \
        "Articles are not appended post 'Load More Stories' button click for " + temp_variable + " page"


def verify_each_article(page, temp_variable):
    print("inside function verify_each_article")
    temp_number = driver.find_elements(By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles are :- ", len(temp_number))
    assert len(temp_number) > 0, "Articles are not present for " + temp_variable + " page"
    count = 0
    time.sleep(5)
    while count < len(temp_number):
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        temp_xpath_img = \
            "(//div[@class='article-card d-flex flex-column col-4 col-desktop-4']/a/img)[" + temp_string + "]"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH, temp_xpath_img)))
        time.sleep(1)
        article_heading = driver.find_element(By.XPATH, temp_xpath_img)
        actions = ActionChains(driver)
        actions.move_to_element(article_heading).perform()
        article = article_heading.get_attribute("title")
        assert article_heading.is_displayed(), \
            "Article heading is not displayed for: " + article + ": article in page :" \
               + page
        print("article is :", article)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          article_heading)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        category_str = "(//div[@class='article-card__categories'])[" + temp_string + "]"
        temp_category = driver.find_element(By.XPATH, category_str)
        print("category is/are :", temp_category.text)
        assert temp_category.text is not None and \
               temp_category.text != "", "Category is not present for " + article + " article in page " + page
        author_str = "(//div[@class='article-card__meta d-flex']/a/span)[" + temp_string + "]"
        temp_author = driver.find_element(By.XPATH, author_str)
        print("author is :", temp_author.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "Author is not present for " + article + " article in page " + page
        # date_str = "(//div[@class='article-card__meta d-flex']/p)[" + temp_string + "]"
        # temp_date = driver.find_element(By.XPATH, date_str)
        # print("date is :", temp_date.text)
        # assert temp_date.text is not None and \
        #        temp_date.text != "", "Date is not present for " + article + " article in page " + page
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        time.sleep(2)
        if page == "WEB SERIES" or page == "TELEVISION":
            time.sleep(3)
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, \
            "for 'Other Trending Black News' section, for :" + article + ": article , title text does not match"
        driver.back()
        temp_title = temp_variable + " - SHADOW & ACT"
        print("title is :- ", temp_title)
        WebDriverWait(driver, 40).until(ec.title_is(temp_title))
        count += 1


def verify_final_article(page, temp_variable):
    temp_string = "7"
    print("tempString : ", temp_string)
    temp_xpath_img = "(//div[@class='article-card d-flex flex-column col-4 col-desktop-4']/a/img)[" + temp_string + "]"
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, temp_xpath_img)))
    time.sleep(4)
    article_heading = driver.find_element(By.XPATH, temp_xpath_img)
    actions = ActionChains(driver)
    actions.move_to_element(article_heading).perform()
    article = article_heading.get_attribute("title")
    assert article_heading.is_displayed(), "Article heading is not displayed for: " + article + ": article in page :" \
                                           + page
    print("article is :", article)
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      article_heading)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed for " + article
    category_str = "(//div[@class='article-card__categories'])[" + temp_string + "]"
    temp_category = driver.find_element(By.XPATH, category_str)
    print("category is/are :", temp_category.text)
    assert temp_category.text is not None and \
           temp_category.text != "", "Category is not present for " + article + " article in page " + page
    author_str = "(//div[@class='article-card__meta d-flex']/a/span)[" + temp_string + "]"
    temp_author = driver.find_element(By.XPATH, author_str)
    print("author is :", temp_author.text)
    assert temp_author.text is not None and \
           temp_author.text != "", "Author is not present for " + article + " article in page " + page
    # date_str = "(//div[@class='article-card__meta d-flex']/p)[" + temp_string + "]"
    # temp_date = driver.find_element(By.XPATH, date_str)
    # print("date is :", temp_date.text)
    # assert temp_date.text is not None and \
    #        temp_date.text != "", "Date is not present for " + article + " article in page " + page
    driver.execute_script("arguments[0].click();", article_heading)
    print("clicked on article heading")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(3)
    print("Current window title: " + driver.title)
    temp_str = driver.title
    temp = temp_str.split(' -')
    compare_1 = str(temp[0])
    compare_2 = article
    print("deduced string is :", compare_1)
    print("text string is :", compare_2)
    assert compare_1 == compare_2, "On" + page + "having article :" + article + ": , title text does not match"
    driver.back()
    temp_title = temp_variable + " - SHADOW & ACT"
    print("title is :- ", temp_title)
    WebDriverWait(driver, 40).until(ec.title_is(temp_title))


def set_status():
    print("Function called set Status")
    driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": '
      '{"status":"passed", "reason": ", for android chrome, on staging.shadowandact.com Film Page do work as expected"}}')


environment()
page_load()
post_page_load_pop_up()
# verify_particular_page("TELEVISION")
verify_particular_page("FILM")
set_status()
driver.quit()
# verify_particular_page("WEB SERIES")
# verify_particular_page("INTERVIEWS")
