from environment import *


def verify_presence_of_element_in_page():
    right_arrow = driver.find_element(By.XPATH, "//button[@id='home-hero-slick-arrow-next']")
    assert right_arrow.is_displayed(), "right arrow element is not present"


def verify_carousel_articles_and_arrows():
    # verify_presence_of_element_in_page()
    print("inside function carousel articles and arrows verification")
    temp_number = driver.find_elements(By.XPATH, "//div[@class='home-hero-card__title']")
    number_of_entries_carousel = len(temp_number)-1
    number_of_entries = int(number_of_entries_carousel/2)
    assert number_of_entries > 0, "articles are not present in carousel"
    print("number of entries in Carousel are :- ", number_of_entries)
    left_click_button = driver.find_element(By.XPATH, "//div[@class='home-hero-slider position-relative']//button[1]")
    assert left_click_button.is_displayed(), "left click arrow button is not displayed in carousel"
    right_click_button = driver.find_element(
       By.XPATH, "//div[@class='home-hero-slider position-relative']//button[2]")
    assert right_click_button.is_displayed(), "right click arrow button is not displayed in carousel"
    if right_click_button.is_displayed() and right_click_button.is_displayed():
        print("both right and left click buttons are displayed on this page")
    count = 1
    time.sleep(2)
    while count < (number_of_entries+1):
        # time.sleep(2)
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        time.sleep(1)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH,
          "(//div[@class='home-hero-card__categories'])["+temp_string+"]")))
        temp_categories = driver.find_element(
          By.XPATH,
          "(//div[@class='home-hero-card__categories'])["+temp_string+"]")
        print("categories for this article in Carousel are :- ", temp_categories.text)
        # assert temp_categories.text is not None and temp_categories.text != \
        #        "", "No Categories are found for this article."
        temp_author = driver.find_element(
          By.XPATH,
          "//div[@class='home-hero-slider position-relative']"
          "//div["+temp_string+"]//div[1]//div[1]//div[1]//div[3]//a[1]")
        print("Author :", temp_author.text)
        assert temp_author.text is not None and temp_author.text != "", "No Author is found for this article."
        temp_date = driver.find_element(
          By.XPATH,
          "//div[@class='home-hero-slider position-relative']"
          "//div["+temp_string+"]//div[1]//div[1]//div[1]//div[3]//p[1]")
        print("Date :", temp_date.text)
        assert temp_date.text is not None and temp_date.text != "", "No Date is found for this article."
        temp_xpath = "(//div[@class='slick-slider slick-initialized']//div[1]//div[1]//div[2]/a[1])["+temp_string+"]"
        actions = ActionChains(driver)
        article_heading = driver.find_element(By.XPATH, temp_xpath)
        assert article_heading.is_displayed(), "article heading is not displayed in carousel"
        article = str(article_heading.text)
        print("article is :", article)
        tmp_img = "(//div[@class='home-hero-card position-relative']/a/img)["+temp_string+"]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, tmp_img)))
        temp_img = driver.find_element(By.XPATH, tmp_img)
        # time.sleep(2)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          temp_img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        actions.move_to_element(article_heading).perform()
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.title_is(article+" - SHADOW & ACT"))
        # time.sleep(1)
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, "for Carousel, for one of the links , title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
        temp = 0
        while temp < count:
            if count >= 6:
                break
            time.sleep(1)
            right_click_button = driver.find_element(
              By.XPATH, "//div[@class='home-hero-slider position-relative']//button[2]")
            right_click_button.click()
            temp += 1
            print("clicked the right icon number of times :- ", temp)
        count += 1


def verify_load_more(number):
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='load more stories']")))
    load_more_stories_button = driver.find_element(By.XPATH, "//button[normalize-space()='load more stories']")
    if number == 8:
        print("when number of articles are :- ", number)
        actions = ActionChains(driver)
        actions.move_to_element(load_more_stories_button).perform()
    if number == 12:
        print("when number of articles are :- ", number)
        time.sleep(2)
        actions = ActionChains(driver)
        actions.move_to_element(load_more_stories_button).perform()
        # time.sleep(1)
        # driver.execute_script("arguments[0].scrollIntoView();", load_more_stories_button)
    load_more_stories_button.click()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='load more stories']")))


def verify_latest_section():
    print("inside function verify_latest_section")
    actions = ActionChains(driver)
    latest_heading = driver.find_element(By.CLASS_NAME, "home-latest-articles-grid__title")
    actions.move_to_element(latest_heading).perform()
    print("heading ", latest_heading.text)
    assert latest_heading.text == "The Latest", "heading 'The Latest' does not match"
    temp_articles_in_latest = driver.find_elements(
      By.XPATH,
      "//div[@class='article-card d-flex flex-column col-4 col-desktop-6']")
    print("number of articles in 'The Latest' section are", len(temp_articles_in_latest))
    assert len(temp_articles_in_latest) > 0, "articles are not present under 'The Latest' section."
    if len(temp_articles_in_latest) == 4:
        count = 0
    elif len(temp_articles_in_latest) == 8:
        count = 4
    elif len(temp_articles_in_latest) == 12:
        count = 8
        time.sleep(2)
    while count < len(temp_articles_in_latest):
        if len(temp_articles_in_latest) == 8 and count != 4:
            verify_load_more(len(temp_articles_in_latest))
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        # time.sleep(1)
        temp_xpath_img = "(//div[@class='article-card d-flex flex-column col-4 col-desktop-6']" \
                         "//a[1]//img[1])["+temp_string+"]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH,
          temp_xpath_img)))
        article_heading_img = driver.find_element(By.XPATH, temp_xpath_img)
        article = article_heading_img.get_attribute("title")
        print("article is :", article)
        time.sleep(1)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          article_heading_img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        actions = ActionChains(driver)
        actions.move_to_element(article_heading_img).perform()
        article = article_heading_img.get_attribute("title")
        print("article is :", article)
        temp_category = driver.find_element(By.XPATH, "(//div[@class='article-card__categories'])["+temp_string+"]")
        print("category :", temp_category.text)
        assert temp_category.text is not None and \
               temp_category.text != "", "Category is not present for : "+article+" article in 'The Latest' section."
        temp_author = driver.find_element(
          By.XPATH,
          "(//div[@class='article-card__meta d-flex']//a)["+temp_string+"]")
        print("temp_author :", temp_author.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "Author is not present for " + article + "article in 'The Latest' section."
        temp_date = driver.find_element(
          By.XPATH,
          "(//div[@class='article-card__meta d-flex']//p)["+temp_string+"]")
        print("temp_date :", temp_date.text)
        assert temp_date.text is not None and \
               temp_date.text != "", "Date is not present for " + article + " article in 'The Latest' section."
        driver.execute_script("arguments[0].click();", article_heading_img)
        print("clicked on article heading")
        WebDriverWait(driver, 10).until(ec.title_is(article+" - SHADOW & ACT"))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, "for 'The Latest', for one of the articles , title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
        time.sleep(1)
        count += 1
        if len(temp_articles_in_latest) == 12:
            break
    # verify_load_more(len(temp_articles_in_latest))
    # verify_post_click_load_more()


def verify_post_click_load_more():
    print("function called verify_post_click_load_more")
    temp_string = "5"
    print("tempString : ", temp_string)
    temp_xpath_img = "(//div[@class='article-card d-flex flex-column col-4 col-desktop-6']" \
                     "//a[1]//img[1])[" + temp_string + "]"
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
      By.XPATH,
      temp_xpath_img)))
    time.sleep(3)
    article_heading_img = driver.find_element(By.XPATH, temp_xpath_img)
    article = article_heading_img.get_attribute("title")
    print("article is :", article)
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      article_heading_img)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed for " + article
    actions = ActionChains(driver)
    actions.move_to_element(article_heading_img).perform()
    article = article_heading_img.get_attribute("title")
    print("article is :", article)
    temp_category = driver.find_element(By.XPATH, "(//div[@class='article-card__categories'])[" + temp_string + "]")
    print("category :", temp_category.text)
    assert temp_category.text is not None and \
           temp_category.text != "", "Category is not present for : " + article + " article in 'The Latest' section."
    temp_author = driver.find_element(
      By.XPATH,
      "(//div[@class='article-card__meta d-flex']//a)[" + temp_string + "]")
    print("temp_author :", temp_author.text)
    assert temp_author.text is not None and \
           temp_author.text != "", "Author is not present for " + article + "article in 'The Latest' section."
    temp_date = driver.find_element(
      By.XPATH,
      "(//div[@class='article-card__meta d-flex']//p)[" + temp_string + "]")
    print("temp_date :", temp_date.text)
    assert temp_date.text is not None and \
           temp_date.text != "", "Date is not present for " + article + " article in 'The Latest' section."
    driver.execute_script("arguments[0].click();", article_heading_img)
    print("clicked on article heading")
    WebDriverWait(driver, 10).until(ec.title_is(article + " - SHADOW & ACT"))
    print("Current window title: " + driver.title)
    temp_str = driver.title
    temp = temp_str.split(' -')
    compare_1 = str(temp[0])
    compare_2 = article
    print("deduced string is :", compare_1)
    print("text string is :", compare_2)
    assert compare_1 == compare_2, "for 'The Latest', for one of the articles , title text does not match"
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))


def verify_load_more_the_latest():
    print("function called verify_load_more")
    temp_articles = driver.find_elements(
      By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-6']")
    print("number of articles before load more buttons click", len(temp_articles))
    number_before_click = len(temp_articles)
    load_more_articles = driver.find_element(By.XPATH, "//button[contains(text(),'load more stories')]")
    actions = ActionChains(driver)
    actions.move_to_element(load_more_articles).perform()
    load_more_articles.click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(
      ec.presence_of_element_located((
        By.XPATH, "//button[contains(text(),'load more stories')]")))
    temp_articles_in_latest_post_click = driver.find_elements(
      By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-6']")
    assert len(temp_articles_in_latest_post_click) > number_before_click, \
        "articles not appended after clicking Load More"


def verify_signup():
    print("in the function verify_signup")
    sign_up_section = driver.find_element(
      By.XPATH, "//div[@class='subscribe-form bg-teal text-white "
                "page-home__subscribe-form d-none d-desktop-block']")
    actions = ActionChains(driver)
    actions.move_to_element(sign_up_section).perform()
    assert sign_up_section.is_displayed(), "Sign Up section is not being displayed"
    sign_up_text = driver.find_element(By.XPATH, "//h3[normalize-space()='Sign up for our weekly newsletter']")
    assert sign_up_text.is_displayed(), "text is displayed for signup section"
    email = driver.find_element(By.XPATH, "//input[@placeholder='Your email']")
    email.send_keys("fortestpurposesonly5@gmail.com")
    submit_button = driver.find_element(By.XPATH, "//input[@value='submit']")
    submit_button.click()


def verify_most_popular():
    print("in the function verify_most_popular section")
    most_popular = driver.find_element(By.XPATH, "//h4[normalize-space()='Most Popular']")
    actions = ActionChains(driver)
    actions.move_to_element(most_popular).perform()
    assert most_popular.is_displayed(), "'Most Popular' heading is not displayed"
    tmp = driver.find_elements(By.CSS_SELECTOR, "div.side-tabs li")
    temp_articles = len(tmp)
    count = 0
    while count < temp_articles:
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        temp_xpath = "//div[@class='flex-full']//li["+temp_string+"]//a"
        WebDriverWait(driver, 40).until(
          ec.presence_of_element_located((
            By.XPATH, temp_xpath)))
        article_heading = driver.find_element(By.XPATH, temp_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(article_heading).perform()
        article = article_heading.get_attribute("title")
        print("article is :", article)
        temp_heading = article + " - SHADOW & ACT"
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.title_is(temp_heading))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, "for 'Most Popular' section, for "\
                                       + article + ": article , title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
        count += 1


def verify_top_articles():
    print("in the function verify_most_popular section")
    temp = driver.find_element(By.XPATH,
                               "//cnx[@class='cnx-main-container cnx-in-desktop cnx-ps cnx-main-container-flex']")
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located((
        By.XPATH,
        "//cnx[@class='cnx-main-container cnx-in-desktop cnx-ps cnx-main-container-flex']")))
    time.sleep(2)
    actions = ActionChains(driver)
    actions.move_to_element(temp).perform()
    assert temp.is_displayed(), "'Top Articles' section is not being displayed"
    assert temp.text is not None and temp.text != "", \
        "header text is missing for Initial article of 'Top Articles' section"
    print("heading for initial article in Top Articles Section is :- ", temp.text)


def verify_shadow_and_act_originals():
    print("inside the function shadow and act originals")
    header = driver.find_element(By.XPATH, "//h2[normalize-space()='S&A Originals']")
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    assert header.is_displayed(), "'S&A Originals' section header is not displayed"
    print("header ", header.text)
    temp_articles_in_sanda_originals = driver.find_elements(
      By.XPATH, "//div[@class='original-article-card d-flex flex-column position-relative']")
    number_or_articles = int(len(temp_articles_in_sanda_originals)/3)
    print("number of articles in 'S&A Originals' section are", number_or_articles)
    assert number_or_articles > 0, "articles are not present under 'The Latest' section."
    count = 0
    while count < number_or_articles:
        temp_string = str(count + 7)
        print("count : ", count)
        print("tempString : ", temp_string)
        time.sleep(1)
        temp_xpath = "(//div[@class='original-article-card__content bg-white d-flex flex-column " \
                     "flex-full position-absolute']/div[2]/a)["+temp_string+"]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, temp_xpath)))
        article_heading = driver.find_element(By.XPATH, temp_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(article_heading).perform()
        article = article_heading.get_attribute("title")
        assert article_heading.is_displayed(), \
            "Article Heading is not displayed for " + article + ": article in 'S&A Originals' section."
        print("article is :", article)
        tmp_img = "(//div[@class='original-article-card d-flex flex-column position-relative']/a/img)["+temp_string+"]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, tmp_img)))
        temp_img = driver.find_element(By.XPATH, tmp_img)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          temp_img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        assert article is not None and article != "", \
            "article heading is not present for one of the links of 'S&A Originals' section."
        temp_category = driver.find_element(
          By.XPATH,
          "(//div[@class='original-article-card__content bg-white d-flex "
          "flex-column flex-full position-absolute']/div[1])["+temp_string+"]")
        print("category :", temp_category.text)
        assert temp_category.text is not None and \
               temp_category.text != "", "Category is not present for "\
                                         + article + ": article in 'S&A Originals' section."
        temp_author = driver.find_element(
          By.XPATH, "(//div[@class='original-article-card__meta d-flex']/a)["+temp_string+"]")
        print("temp_author :", temp_author.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "Author is not present for " + article + "article in 'S&A Originals' section."
        temp_date = driver.find_element(
          By.XPATH, "(//div[@class='original-article-card__meta d-flex']/p)["+temp_string+"]")
        print("temp_date :", temp_date.text)
        assert temp_date.text is not None and \
               temp_date.text != "", "Date is not present for " + article + " article in 'S&A Originals' section."
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.title_is(article+" - SHADOW & ACT"))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, "for 'S&A Originals', for article "+article+" , title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
        count += 1


def verify_post_click_more_originals_number_comparison():
    time.sleep(3)
    print("inside function post_click_more_originals_number_comparison")
    see_more_originals_button = driver.find_element(By.XPATH, "//button[contains(text(),'See More Originals')]")
    actions = ActionChains(driver)
    actions.move_to_element(see_more_originals_button).perform()
    temp_articles_in_sanda_originals = driver.find_elements(
      By.XPATH, "//div[@class='original-article-card d-flex flex-column position-relative']")
    number_or_articles_before_click = int(len(temp_articles_in_sanda_originals) / 3)
    assert number_or_articles_before_click > 0, "articles are not present under 'S&A Originals' section."
    print("number of articles in 'S&A Originals' section before click are", number_or_articles_before_click)
    see_more_originals_button.click()
    time.sleep(3)
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'See More Originals')]")))
    temp_articles_in_sanda_originals_post_click = driver.find_elements(
      By.XPATH, "//div[@class='original-article-card d-flex flex-column position-relative']")
    number_or_articles_post_click = int(len(temp_articles_in_sanda_originals_post_click) / 3)
    print("number of articles in 'S&A Originals' section post click are", number_or_articles_post_click)
    assert number_or_articles_post_click > \
           number_or_articles_before_click, "after clicking 'SEE MORE" \
                                            " ORIGINALS' once number of articles do not increase"
    see_more_originals_button.click()
    WebDriverWait(driver, 40).until(ec.title_is("S&A Originals - SHADOW & ACT"))
    assert driver.title == "S&A Originals - SHADOW & ACT", \
        "after clicking 'See More Originals' " \
        "twice, 'S&A Originals' page is not loaded"
    driver.back()
    time.sleep(1)


def verify_other_trending_black_news():
    print("inside function verify_other_trending_black_news")
    other_trending_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Other Trending Black News')]")
    actions = ActionChains(driver)
    actions.move_to_element(other_trending_header).perform()
    assert other_trending_header.is_displayed(), "header is not present for 'Other Trending Black News'"
    other_trending_stories = driver.find_elements(By.CLASS_NAME, "col-desktop-3")
    print("number of articles in other trending black news are :", len(other_trending_stories))
    count = 0
    while count < len(other_trending_stories):
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        temp_xpath_img = "(//div[@class='other-article-card']/a/img)["+temp_string+"]"
        WebDriverWait(driver, 40).until(
          ec.presence_of_element_located((By.XPATH, temp_xpath_img)))
        # time.sleep(2)
        article_heading = driver.find_element(By.XPATH, temp_xpath_img)
        actions = ActionChains(driver)
        actions.move_to_element(article_heading).perform()
        article = article_heading.get_attribute("title")
        print("article is :", article)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, temp_xpath_img)))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth != "
          "\"undefined\" && arguments[0].naturalWidth > 0",
          article_heading)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        other_temp_str = "(//div[@class='other-article-card']/a)["+temp_string+"]"
        other_site_attr = driver.find_element(By.XPATH, other_temp_str)
        other_site_heading = other_site_attr.get_attribute("title")
        other_site = other_site_attr.get_attribute("href")
        print("other site heading is :- ", other_site_heading)
        print("other site is :- ", other_site)
        category = driver.find_element(By.XPATH, "(//div[@class='other-article-card']/div[1]/a)["+temp_string+"]")
        print("category is ", category.text)
        assert category.text is not None and \
               category.text != "", "Category is not present for " \
                                    + article + ": article in 'other trending black news' section."
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        # switch to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        # assert "Podcast" in driver.title
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, \
            "for 'Other Trending Black News' section, for " + article + ": article , title text does not match"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
        count += 1


# environment()
# page_load()
# post_page_load_pop_up()
# verify_carousel_articles_and_arrows()
# verify_latest_section()
# verify_top_articles()
# verify_signup()
# verify_most_popular()
# verify_shadow_and_act_originals()
# verify_post_click_more_originals_number_comparison()
# verify_other_trending_black_news()
