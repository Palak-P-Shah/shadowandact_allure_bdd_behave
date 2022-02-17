from environment import *


def verify_nav_bar_presence():
    print("check whether nav bar is present or not")
    time.sleep(3)
    nav_bar = driver.find_element(By.XPATH, "//ul[@class='navbar-nav d-desktop-flex align-items-center']")
    print(nav_bar.text)
    assert nav_bar.text != "" and nav_bar.text is not None, "Nav Bar is not present"
    if (nav_bar.text is not None) or (nav_bar.text != ""):
        print("Nav Bar is present")


def verify_nav_film_link():
    print("checking the Film tab")
    film_link = driver.find_element(By.XPATH, "//a[normalize-space()='FILM']")
    assert film_link.is_displayed(), "Film link is not displayed"
    film_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Film - SHADOW & ACT"))
    assert driver.title == "Film - SHADOW & ACT", "title text for ShadowAndAct does not match"
    print("Current Window Title for Film Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_nav_tv_link():
    print("checking the Television link")
    tv_link = driver.find_element(By.XPATH, "//a[normalize-space()='TELEVISION']")
    assert tv_link.is_displayed(), "Television link is not displayed"
    tv_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Television - SHADOW & ACT"))
    assert driver.title == "Television - SHADOW & ACT", "title for Television link text does not match"
    print("Current Window Title for Television Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_nav_web_series_link():
    print("checking the web series tab")
    web_series_link = driver.find_element(By.XPATH, "//a[normalize-space()='WEB SERIES']")
    assert web_series_link.is_displayed(), "WEB SERIES link is not displayed"
    web_series_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Web Series - SHADOW & ACT"))
    assert driver.title == "Web Series - SHADOW & ACT", "title text for WebSeries does not match"
    print("Current Window Title for WEB SERIES Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_nav_interviews_link():
    interviews_link = driver.find_element(By.XPATH, "//a[normalize-space()='INTERVIEWS']")
    assert interviews_link.is_displayed(), "Interviews link is not displayed"
    interviews_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Interviews - SHADOW & ACT"))
    assert driver.title == "Interviews - SHADOW & ACT", "title text for Interviews page does not match"
    print("Current Window Title for Interviews Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_podcast_link():
    podcast_link = driver.find_element(By.XPATH, "//a[normalize-space()='PODCAST']")
    assert podcast_link.is_displayed(), "Podcast link is not displayed"
    podcast_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Opening Act Podcast"))
    assert "Podcast" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Podcast is working as expected")


def verify_rising_awards_link():
    rising_awards_link = driver.find_element(By.XPATH, "//a[normalize-space()='RISING AWARDS']")
    assert rising_awards_link.is_displayed(), "Rising Awards link is not displayed"
    rising_awards_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("RISING Awards Digital 2021 - SHADOW & ACT"))
    assert driver.title == "RISING Awards Digital 2021 - SHADOW & ACT", \
        "title text for Rising Awards page does not match"
    print("Current Window Title for Rising Awards Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_nav_search_bar():
    search_bar = driver.find_element(
      By.XPATH,
      "//button[@type='submit']//*[name()='svg']")
    assert search_bar.is_displayed(), "Search Bar is not displayed"
    search_bar.click()
    input_search = driver.find_element(By.XPATH, "//input[@type='text']")
    search_text = "Web Series"
    input_search.send_keys(search_text)
    search_bar.click()
    # WebDriverWait(driver, 40).until(ec.url_contains(search_text))
    WebDriverWait(driver, 40).until(ec.title_is("Search - SHADOW & ACT"))
    assert driver.title == "Search - SHADOW & ACT", "title text does not match for search page"
    print("Current window title for Search Page is: " + driver.title)
    print("link for Search is present and working as expected")


def verify_footer_instagram_link():
    footer_instagram = driver.find_element(
      By.XPATH, "//a[@class='sa-footer__social-link sa-footer__social-link--instagram']")
    assert footer_instagram.is_displayed(), "Footer - Instagram link is not displayed"
    footer_instagram.click()
    print("clicked on instagram link")
    verify_shadowandact_footer_instagram()


def verify_shadowandact_footer_instagram():
    print("inside function footer instagram link")
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Instagram"))
    assert "Instagram" in driver.title, "title does not contain Instagram"
    # assert driver.current_url == 'https://www.instagram.com/shadow_act/', "instagram link in footer is not active"
    # if driver.current_url == 'https://www.instagram.com/shadow_act/':
    #     print("instagram link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_footer_twitter_link():
    twitter_link = driver.find_element(By.XPATH, "//a[@class='sa-footer__social-link sa-footer__social-link--twitter']")
    assert twitter_link.is_displayed(), "Footer - Twitter link is not displayed"
    twitter_link.click()
    print("clicked on footer twitter link")
    verify_shadowandact_footer_twitter()


def verify_shadowandact_footer_twitter():
    print("inside function footer twitter link")
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Shadow and Act"))
    assert driver.current_url == 'https://twitter.com/shadowandact/', "twitter link in footer is not active"
    if driver.current_url == 'https://twitter.com/shadowandact/':
        print("twitter link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_shadowandact_footer_facebook_link():
    print("inside function footer facebook link")
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Shadow And Act"))
    assert driver.current_url == 'https://www.facebook.com/shadowandact/', "facebook link in footer is not active"
    if driver.current_url == 'https://www.facebook.com/shadowandact/':
        print("face book link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_footer_facebook_link():
    facebook_footer_link = driver.find_element(
       By.XPATH, "//a[@class='sa-footer__social-link sa-footer__social-link--facebook']//*[name()='svg']")
    assert facebook_footer_link.is_displayed(), "Facebook footer link is not displayed"
    facebook_footer_link.click()
    print("clicked on facebook link")
    verify_shadowandact_footer_facebook_link()


def verify_nav_bar_links():
    print("check whether each nav bar link is present and working, total 7 links")
    verify_nav_film_link()
    verify_nav_tv_link()
    verify_nav_web_series_link()
    verify_nav_interviews_link()
    verify_podcast_link()
    verify_rising_awards_link()
    verify_nav_search_bar()
    print("All 7 links :- FILM, TELEVISION, WEB SERIES, INTERVIEWS, PODCAST, RISING AWARDS, Search"
          "are working as expected.")
    verify_footer_presence()


def verify_footer_presence():
    time.sleep(3)
    footer_sanda_page = driver.find_element(
      By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    assert footer_sanda_page.is_displayed(), "Footer section for SHADOWANDACT is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(footer_sanda_page).perform()
    if footer_sanda_page.is_displayed():
        print("footer section is displayed on shadowandact page")


def verify_footer_home_link():
    print("within function verify_footer_home_link ")
    home_link = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
    assert home_link.is_displayed(), "footer home link is not displayed"
    home_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
    assert driver.title == "SHADOW & ACT", "title text is not matching"


def verify_footer_privacy_link():
    print("within function verify_footer_privacy_link ")
    privacy_link = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy']")
    actions = ActionChains(driver)
    actions.move_to_element(privacy_link).perform()
    assert privacy_link.is_displayed(), "footer privacy link is not displayed"
    privacy_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Privacy is working as expected")


def verify_footer_careers_link():
    print("within function verify_footer_careers_link")
    careers_link = driver.find_element(By.XPATH, "//a[normalize-space()='Careers']")
    assert careers_link.is_displayed(), "footer careers link is not displayed"
    careers_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Careers is working as expected")


def verify_footer_partner_with_us_link():
    print("within function verify_footer_partner_with_us_link")
    partner_with_us_link = driver.find_element(By.XPATH, "//a[normalize-space()='Partner With Us']")
    assert partner_with_us_link.is_displayed(), "footer partner with us link is not displayed"
    partner_with_us_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Partner with us is working as expected")


def verify_footer_blavity_link():
    print("within function verify_footer_blavity_link")
    blavity_link = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity']")
    assert blavity_link.is_displayed(), "footer partner with us link is not displayed"
    blavity_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Blavity is working as expected")


def verify_footer_afrotech_link():
    print("within function verify_footer_afrotech_link")
    afrotech_link = driver.find_element(By.XPATH,
                                        "//a[@class='sa-footer__link font-secondary'][normalize-space()='AfroTech']")
    assert afrotech_link.is_displayed(), "footer Afrotech link is not displayed"
    afrotech_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("AfroTech"))
    assert "AfroTech" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for afrotech is working as expected")


def verify_footer_21_ninety_link():
    print("within function verify_footer_21_ninety_link")
    twenty_one_ninety_link = driver.find_element(By.XPATH, "//a[normalize-space()='21Ninety']")
    assert twenty_one_ninety_link.is_displayed(), "footer Afrotech link is not displayed"
    twenty_one_ninety_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("21Ninety"))
    assert "21Ninety" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for 21Ninety is working as expected")


def verify_footer_travel_noire_link():
    print("within function verify_footer_travel_noire_link")
    travel_noire_link = driver.find_element(By.XPATH, "//a[@class='sa-footer__link font-secondary']"
                                                      "[normalize-space()='Travel Noire']")
    assert travel_noire_link.is_displayed(), "footer Travel Noire link is not displayed"
    travel_noire_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Travel Noire"))
    assert "Travel Noire" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Travel Noire is working as expected")


def verify_footer_links():
    print("check whether footer links are working as expected")
    footer_link = driver.find_element(By.XPATH, "//body/div[@id='__nuxt']/div[@id='__layout']/div[1]"
                                                "/footer[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
    actions = ActionChains(driver)
    actions.move_to_element(footer_link).perform()
    assert footer_link.is_displayed(), "footer link is not displayed for SHADOW AND ACT"
    footer_link.click()
    footer_sanda_page = driver.find_element(
      By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    assert footer_sanda_page.is_displayed(), "footer copyright text is not displayed for SHADOW AND ACT"
    actions = ActionChains(driver)
    actions.move_to_element(footer_sanda_page).perform()
    verify_footer_home_link()
    verify_footer_privacy_link()
    verify_footer_careers_link()
    verify_footer_partner_with_us_link()
    verify_footer_blavity_link()
    verify_footer_afrotech_link()
    verify_footer_21_ninety_link()
    verify_footer_travel_noire_link()
    verify_footer_facebook_link()
    verify_footer_twitter_link()
    verify_footer_instagram_link()


def launch_url(slug_value):
    formed_url = url_name + slug_value
    print("1: formed url: ", formed_url)
    assert formed_url is not None and formed_url != "", "formed url with slug is not appropriate"
    driver.get(formed_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    print("2 : page is loaded")


def verify_slug_comparison():
    print("title of the page ", driver.title)
    temp_split = driver.title.split(" -")
    print("temp_split :", temp_split[0])
    web_element_title = driver.find_element(By.CLASS_NAME, "article-title")
    print("webelement title :", web_element_title.text)
    article_title_str = web_element_title.text
    assert article_title_str == temp_split[0], "article title and title of the page do not match"
    if article_title_str == temp_split[0]:
        print("article title and title of the page do match")
    # assert_equal(article_title_str, temp_split[0])
    print("3 : verification done for comparison of page(driver) title and article title")


def verify_read_full_article_button():
    read_full_article_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Read Full Article'])[1]")
    assert read_full_article_button.is_displayed(), "Read Full Article Button is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(read_full_article_button).perform()
    try:
        pop_up_close_button = driver.find_element(By.XPATH, "//img[@data-pin-nopin='true']")
        if pop_up_close_button.is_displayed():
            pop_up_close_button.click()
            print("clicked on close button of pop up")
    # NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("pop-up does not exist")
    if read_full_article_button.is_displayed():
        print("4. Read Full Article Button is displayed")
        read_full_article_button.click()
        WebDriverWait(driver, 40).until(
          ec.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Read Comments')])[1]")))


def verify_read_comments_button():
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Read Comments')])[1]")))
    # time.sleep(2)
    read_comments_button = driver.find_element(By.XPATH, "(//span[contains(text(),'Read Comments')])[1]")
    assert read_comments_button.is_displayed(), "Read Comments Button is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(read_comments_button).perform()
    read_comments_button.click()
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Hide Comments')]")))
    hide_comments_button = driver.find_element(By.XPATH, "//span[contains(text(),'Hide Comments')]")
    assert hide_comments_button.is_displayed(), "Read Comments Button is not displayed"
    if hide_comments_button.is_displayed():
        print("5. comments are loaded")


def verify_navigation_slug_and_page_load(slug_value):
    print("in the function verify_navigation_slug_and_page_load and value is :", slug_value)
    launch_url(slug_value)
    verify_slug_comparison()
    verify_read_full_article_button()
    verify_read_comments_button()


def exit_browser():
    print("closing the browser instance")
    driver.quit()


# environment()
# page_load()
# post_page_load_pop_up()
# verify_nav_bar_links()
