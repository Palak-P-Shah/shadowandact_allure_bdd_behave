from environment import *


def verify_header_section():
    print("function called verify_header_section")
    header_question = driver.find_element(
      By.CSS_SELECTOR,
      "div[class='slick-slide slick-active slick-current'] div h3[class='ra-hero__card__title']")
    assert header_question.is_displayed(), "Header rhs question is not displayed"
    header_slick_dots = driver.find_element(By.XPATH, "//ul[@class='slick-dots']")
    assert header_slick_dots.is_displayed(), "Header slick dots are not displayed"
    # time.sleep(2)
    header_description = driver.find_element(
      By.XPATH,
      "//div[@class='slick-slide slick-active slick-current']//div//p[@class='ra-hero__card__description']")
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located(
        (By.XPATH,
         "//div[@class='slick-slide slick-active slick-current']//div//p[@class='ra-hero__card__description']")))
    # actions = ActionChains(driver)
    # actions.move_to_element(header_description).perform()
    assert header_description.is_displayed(), "Header description is not displayed for first slide"
    slick_dot_2 = driver.find_element(By.XPATH, "//button[normalize-space()='2']")
    slick_dot_2.click()
    time.sleep(1)
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located(
        (By.CSS_SELECTOR, "div[class='slick-slide slick-active slick-current'] div h3[class='ra-hero__card__title']")))
    header_2 = driver.find_element(
      By.CSS_SELECTOR,
      "div[class='slick-slide slick-active slick-current'] div h3[class='ra-hero__card__title']")
    assert header_2.is_displayed(), "Header rhs for second slick dot is not displayed"
    header_description = driver.find_element(
      By.XPATH,
      "//div[@class='slick-slide slick-active slick-current']//div//p[@class='ra-hero__card__description']")
    assert header_description.is_displayed(), "Header description is not displayed for second slide"
    slick_dot_3 = driver.find_element(By.XPATH, "//button[normalize-space()='3']")
    slick_dot_3.click()
    time.sleep(1)
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located(
        (By.CSS_SELECTOR, "div[class='slick-slide slick-active slick-current'] div h3[class='ra-hero__card__title']")))
    header_3 = driver.find_element(
      By.CSS_SELECTOR,
      "div[class='slick-slide slick-active slick-current'] div h3[class='ra-hero__card__title']")
    assert header_3.is_displayed(), "Header rhs for second slick dot is not displayed"
    header_description = driver.find_element(
      By.XPATH,
      "//div[@class='slick-slide slick-active slick-current']//div//p[@class='ra-hero__card__description']")
    assert header_description.is_displayed(), "Header description is not displayed for third slide"


def verify_each_job_post_in_behind_the_scenes_grid():
    print("inside function verify_each_job_post_in__behind_the_scenes_grid")
    number = 1
    time.sleep(3)
    while 9 > number:
        content = driver.find_element(By.XPATH, "(//div[@class='ra-nominee-card__content'])["+str(number)+"]")
        print("content txt is: ", content.text)
        assert content.text is not None and content.text != "", \
            "for one of the post the content 'Job Post, Name, Description' is missing"
        job_title = driver.find_element(By.XPATH, "(//h6[@class='ra-nominee-card__title'])[" + str(number) + "]")
        assert job_title.text is not None and job_title.text != "", \
            "for one of the post" \
            + content.text +\
            " the 'Job Post title' is missing"
        print("Job Title :", job_title.text)
        name = driver.find_element(By.XPATH, "(//h5[@class='ra-nominee-card__name'])[" + str(number) + "]")
        assert name.text is not None and name.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'name' is missing"
        print("Name :", name.text)
        desc = driver.find_element(By.XPATH, "(//p[@class='ra-nominee-card__description'])[" + str(number) + "]")
        assert desc.text is not None and desc.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'description' is missing"
        print("desc :", desc.text)
        img_str = "(//img[@title='"+name.text+"'])[1]"
        img = driver.find_element(By.XPATH, img_str)
        assert img.is_displayed(), \
            "image is not displayed for: "+content.text+":under 'behind the scenes' tab for page Rising Awards"

        img = driver.find_element(By.XPATH,
                                  "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth != "
          "\"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + content.text
        number += 1


def verify_grid_behind_the_scenes():
    print("inside function verify_grid_behind_the_scenes")
    button_behind_the_scenes = driver.find_element(
      By.XPATH,
      "//button[@class='ra-categories__tab-button--active ra__bg--green ra__green']//span[1]")
    button_behind_the_scenes.click()
    time.sleep(1)
    title = driver.find_element(By.XPATH, "(//h3[@class='ra-category-panel__title'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(title).perform()
    assert title.is_displayed(), "Title is missing for 'behind the scenes' grid tab of 'Rising Awards' page"
    right_info = driver.find_element(
      By.XPATH,
      "//div[@class='ra-category-panel ra__bg-desktop--green ra__bg-gradient--green']"
      "//div[@class='ra-category-panel__info']")
    actions.move_to_element(right_info).perform()
    assert right_info.is_displayed(), "right info is missing for 'behind the scenes' grid tab of 'Rising Awards' page"
    assert right_info.text is not None and right_info.text != "", \
        "right info text is missing for 'behind the scenes' grid tab of 'Rising Awards' page"
    print(right_info.text)
    job_post_grid = driver.find_element(
      By.XPATH,
      "//div[@class='ra__green']//div[@class='ra-categories__nominees-desktop d-none d-desktop-grid']")
    actions.move_to_element(job_post_grid).perform()
    assert \
        job_post_grid.is_displayed(), \
        "Job Post image, name, post, etc  is missing " \
        "for 'behind the scenes' grid tab of 'Rising Awards' page"
    verify_each_job_post_in_behind_the_scenes_grid()


def verify_each_job_post_in_actors_grid():
    print("inside function verify_each_job_post_in_actors_grid")
    number = 27
    while 35 > number:
        content = driver.find_element(
          By.XPATH,
          "(//div[@class='ra-nominee-card ra-categories__nominee-card'])["+str(number)+"]")
        print("content txt is: ", content.text)
        assert content.text is not None and content.text != "", \
            "for one of the post the content Job Post, Name, Description' is missing"
        job_title = driver.find_element(By.XPATH, "(//h6[@class='ra-nominee-card__title'])[" + str(number) + "]")
        assert job_title.text is not None and job_title.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'Job Post title' is missing"
        print("Job Title :", job_title.text)
        name = driver.find_element(By.XPATH, "(//h5[@class='ra-nominee-card__name'])[" + str(number) + "]")
        assert name.text is not None and name.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'name' is missing"
        print("Name :", name.text)
        desc = driver.find_element(By.XPATH, "(//p[@class='ra-nominee-card__description'])[" + str(number) + "]")
        assert desc.text is not None and desc.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'description' is missing"
        print("desc :", desc.text)
        img_str = "(//img[@title='" + name.text + "'])[1]"
        img = driver.find_element(By.XPATH, img_str)
        assert img.is_displayed(), "image is not displayed for: " \
                                   + content.text + ":under 'Actors' tab for page Rising Awards"

        img = driver.find_element(By.XPATH,
                                  "(//div[@class='ra-nominee-card__avatar-wrapper']/img)["+str(number)+"]")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, "(//div[@class='ra-nominee-card__avatar-wrapper']/img)["+str(number)+"]")))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth != "
          "\"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + content.text

        number += 1


def verify_grid_actors():
    print("inside function verify_grid_actors")
    grid = driver.find_element(By.XPATH, "//div[@class='ra-categories__tab-buttons d-none d-desktop-grid']")
    actions = ActionChains(driver)
    actions.move_to_element(grid).perform()
    actors_tab = driver.find_element(
      By.XPATH,
      "//button[@class='ra-categories__tab-button ra__purple']//span[contains(text(),'Actors')]")
    actors_tab.click()
    time.sleep(1)
    title = driver.find_element(By.XPATH, "(//h3[@class='ra-category-panel__title'])[2]")
    actions = ActionChains(driver)
    actions.move_to_element(title).perform()
    assert title.is_displayed(), "Title is missing for 'Actors' grid tab of 'Rising Awards' page"
    right_info = driver.find_element(
      By.XPATH,
      "(//div[@class='ra-category-panel__info'])[2]")
    actions.move_to_element(right_info).perform()
    assert right_info.is_displayed(), "right info is missing for 'Actors' grid tab of 'Rising Awards' page"
    assert right_info.text is not None and right_info.text != "", \
        "right info text is missing for 'Actors' grid tab of 'Rising Awards' page"
    print(right_info.text)
    job_post_grid = driver.find_element(
      By.XPATH,
      "(//div[@class='ra__purple'])[1]")
    actions.move_to_element(job_post_grid).perform()
    assert \
        job_post_grid.is_displayed(), \
        "Job Post image, name, post, etc  is missing " \
        "for 'Actors' grid tab of 'Rising Awards' page"
    verify_each_job_post_in_actors_grid()


def verify_each_job_post_in_executives_grid():
    print("function called verify_each_job_post_in_executives_grid")
    number = 53
    while 61 > number:
        content = driver.find_element(By.XPATH, "(//div[@class='ra-nominee-card ra-categories__nominee-card'])[" + str(
          number) + "]")
        print("content txt is: ", content.text)
        assert content.text is not None and content.text != "", \
            "for one of the post the content Job Post, Name, Description' is missing"
        job_title = driver.find_element(By.XPATH, "(//h6[@class='ra-nominee-card__title'])[" + str(number) + "]")
        assert job_title.text is not None and job_title.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'Job Post title' is missing"
        print("Job Title :", job_title.text)
        name = driver.find_element(By.XPATH, "(//h5[@class='ra-nominee-card__name'])[" + str(number) + "]")
        assert name.text is not None and name.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'name' is missing"
        print("Name :", name.text)
        desc = driver.find_element(By.XPATH, "(//p[@class='ra-nominee-card__description'])[" + str(number) + "]")
        assert desc.text is not None and desc.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'description' is missing"
        print("desc :", desc.text)
        img_str = "(//img[@title='" + name.text + "'])[1]"
        img = driver.find_element(By.XPATH, img_str)
        assert img.is_displayed(), "image is not displayed for: " + content.text + \
                                   ":under 'Executives' tab for page 'Rising Awards'"

        img = driver.find_element(By.XPATH,
                                  "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth != "
          "\"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + content.text

        number += 1


def verify_grid_executives():
    print("function called verify_grid_executives")
    grid = driver.find_element(By.XPATH, "//div[@class='ra-categories__tab-buttons d-none d-desktop-grid']")
    actions = ActionChains(driver)
    actions.move_to_element(grid).perform()
    executives_tab = driver.find_element(
      By.XPATH,
      "//button[@class='ra-categories__tab-button ra__red']//span[contains(text(),'Executives')]")
    executives_tab.click()
    time.sleep(1)
    title = driver.find_element(By.XPATH, "(//h3[@class='ra-category-panel__title'])[3]")
    actions = ActionChains(driver)
    actions.move_to_element(title).perform()
    assert title.is_displayed(), "Title is missing for 'Executives' grid tab of 'Rising Awards' page"
    right_info = driver.find_element(
      By.XPATH,
      "(//div[@class='ra-category-panel__info'])[3]")
    actions.move_to_element(right_info).perform()
    assert right_info.is_displayed(), "right info is not displayed for 'Executives' grid tab of 'Rising Awards' page"
    assert right_info.text is not None and right_info.text != "", \
        "right info text is missing for 'Executives' grid tab of 'Rising Awards' page"
    print(right_info.text)
    job_post_grid = driver.find_element(
      By.XPATH,
      "//div[@class='ra__red']//div[@class='ra-categories__nominees-desktop d-none d-desktop-grid']")
    actions.move_to_element(job_post_grid).perform()
    assert \
        job_post_grid.is_displayed(), \
        "Job Post image, name, post, etc  is missing " \
        "for 'Executives' grid tab of 'Rising Awards' page"
    verify_each_job_post_in_executives_grid()


def verify_each_job_post_in_creators_grid():
    print("function called verify_each_job_post_in_creators_grid")
    number = 79
    while 87 > number:
        content = driver.find_element(By.XPATH, "(//div[@class='ra-nominee-card ra-categories__nominee-card'])[" + str(
          number) + "]")
        # print("content txt is: ", content.text)
        assert content.text is not None and content.text != "", \
            "for one of the post the content Job Post, Name, Description' is missing"
        job_title = driver.find_element(By.XPATH, "(//h6[@class='ra-nominee-card__title'])[" + str(number) + "]")
        assert job_title.text is not None and job_title.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'Job Post title' is missing"
        print("Job Title :", job_title.text)
        name = driver.find_element(By.XPATH, "(//h5[@class='ra-nominee-card__name'])[" + str(number) + "]")
        assert name.text is not None and name.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'name' is missing"
        print("Name :", name.text)
        desc = driver.find_element(By.XPATH, "(//p[@class='ra-nominee-card__description'])[" + str(number) + "]")
        assert desc.text is not None and desc.text != "", \
            "for one of the post" \
            + content.text + \
            " the 'description' is missing"
        print("desc :", desc.text)
        img_str = "(//img[@title='" + name.text + "'])[1]"
        img = driver.find_element(By.XPATH, img_str)
        assert img.is_displayed(), "image is not displayed for: " + content.text + \
                                   ":under 'Creators' tab for page 'Rising Awards'"

        img = driver.find_element(By.XPATH,
                                  "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, "(//div[@class='ra-nominee-card__avatar-wrapper']/img)[" + str(number) + "]")))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + content.text

        number += 1


def verify_grid_creators():
    print("function called verify_grid_creators")
    grid = driver.find_element(By.XPATH, "//div[@class='ra-categories__tab-buttons d-none d-desktop-grid']")
    actions = ActionChains(driver)
    actions.move_to_element(grid).perform()
    creators_tab = driver.find_element(
      By.XPATH,
      "//button[@class='ra-categories__tab-button ra__grey']//span[contains(text(),'Creators')]")
    creators_tab.click()
    time.sleep(1)
    title = driver.find_element(By.XPATH, "(//h3[@class='ra-category-panel__title'])[4]")
    actions = ActionChains(driver)
    actions.move_to_element(title).perform()
    assert title.is_displayed(), "Title is missing for 'Creators' grid tab of 'Rising Awards' page"
    right_info = driver.find_element(
      By.XPATH,
      "(//div[@class='ra-category-panel__info'])[4]")
    actions.move_to_element(right_info).perform()
    assert right_info.is_displayed(), "right info is not displayed for 'Creators' grid tab of 'Rising Awards' page"
    assert right_info.text is not None and right_info.text != "", \
        "right info text is missing for 'Creators' grid tab of 'Rising Awards' page"
    print(right_info.text)
    job_post_grid = driver.find_element(
      By.XPATH,
      "//div[@class='ra__grey']//div[@class='ra-categories__nominees-desktop d-none d-desktop-grid']")
    actions.move_to_element(job_post_grid).perform()
    assert \
        job_post_grid.is_displayed(), \
        "Job Post image, name, post, etc  is missing " \
        "for 'Creators' grid tab of 'Rising Awards' page"
    verify_each_job_post_in_creators_grid()


def verify_grid_game_changer():
    print("function called verify_grid_game_changer")
    grid = driver.find_element(By.XPATH, "//div[@class='ra-categories__tab-buttons d-none d-desktop-grid']")
    actions = ActionChains(driver)
    actions.move_to_element(grid).perform()
    game_changer_tab = driver.find_element(
      By.XPATH,
      "//button[@class='ra-categories__tab-button ra__black']//span[contains(text(),'Game-Changer')]")
    game_changer_tab.click()
    time.sleep(1)
    title = driver.find_element(By.XPATH, "(//h3[@class='ra-category-panel-single__title'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(title).perform()
    print(title.text)
    assert title.is_displayed(), "Title is missing for 'Game Changer' grid tab of 'Rising Awards' page"
    right_info = driver.find_element(
      By.XPATH,
      "//div[@class='ra-category-panel-single__info']")
    actions.move_to_element(right_info).perform()
    assert right_info.is_displayed(), "right info is not displayed for 'Game Changer' grid tab of 'Rising Awards' page"
    assert right_info.text is not None and right_info.text != "", \
        "right info text is missing for 'Game Changer' grid tab of 'Rising Awards' page"
    print(right_info.text)
    img = driver.find_element(By.XPATH,
                              "//div[@class='ra-category-panel-single__honoree-avatar']/img")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
      By.XPATH, "//div[@class='ra-category-panel-single__honoree-avatar']/img")))
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      img)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed for Game Changer"


def verify_categories_grid():
    print("inside function categories grid")
    grid = driver.find_element(By.XPATH, "//div[@class='ra-categories__tab-buttons d-none d-desktop-grid']")
    actions = ActionChains(driver)
    actions.move_to_element(grid).perform()
    assert grid.is_displayed(), "Categories Grid is not displayed on the Rising Awards page"
    assert grid.text is not None and grid.text != "", "Categories Grid headers are not present for Rising Awards page"
    print(grid.text)
    verify_grid_behind_the_scenes()
    verify_grid_actors()
    verify_grid_executives()
    verify_grid_creators()
    verify_grid_game_changer()


def verify_bottom_section():
    print("function called verify_s_and_a_rising_awards")
    img = driver.find_element(By.XPATH, "(//img[@class='d-block w-100'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(img).perform()
    assert img.is_displayed(), \
        "image on left for bottom section of 2019 Rising awards is not displayed on the Rising Awards page"
    txt = driver.find_element(By.XPATH, "//h4[contains(text(),'“It is a dream really because ever since I have st')]")
    print(txt.text)
    assert img.is_displayed(), \
        "txt on right for bottom section of 2019 Rising awards is not displayed on the Rising Awards page"
    by = driver.find_element(By.XPATH, "//h5[@class='ra-testimonial__info text-uppercase']")
    print(by.text)
    assert by.is_displayed(), \
        "txt on right for bottom section of 2019 Rising awards is not displayed on the Rising Awards page"


def verify_s_and_a_rising_awards():
    print("function called verify_s_and_a_rising_awards")
    header = driver.find_element(By.XPATH, "//h2[normalize-space()='S&A RISING AWARDS 2019']")
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    assert header.is_displayed(), "header for 2019 Rising awards is not displayed on the Rising Awards page"
    assert header.text is not None and header.text != "", \
        "'2019 Rising Awards' header is not present for Rising Awards page"
    text = driver.find_element(By.XPATH, "//h3[normalize-space()='When outside was open open.']")
    actions.move_to_element(text).perform()
    video_section = driver.find_element(
      By.XPATH,
      "//div[@class='ra-videos__slick slick-slider slick-initialized']//div[@class='slick-track']")
    assert video_section.is_displayed(), \
        "video section for 2019 Rising awards is not displayed on the Rising Awards page"
    number = 1
    while 4 > number:
        print("number ", number)
        video = driver.find_element(
          By.XPATH,
          "//section[@class='ra-videos ra__bg--purple text-center text-white']//div["+str(number)+"]")
        assert video.is_displayed(), "particular video :"\
                                     + str(number) +\
                                     " : under 2019 Rising awards is not displayed on the Rising Awards page"
        actions.move_to_element(video).perform()
        image = driver.find_element(By.XPATH, "(//img[@class='ra-video-card__image'])["+str(number)+"]")
        assert image.is_displayed(), \
            "for video section of 2019 Rising awards image is not displayed on the Rising Awards page"
        button = driver.find_element(
          By.XPATH,
          "(//button[@class='ra-video-card__play d-none d-desktop-block'])["+str(number)+"]")
        button.click()
        time.sleep(5)
        actions.send_keys(Keys.ESCAPE).perform()
        assert button.is_displayed(), \
            "for video section of 2019 Rising awards play button " \
            "for "+str(number)+" video is not displayed on the Rising Awards page"
        txt = driver.find_element(
          By.XPATH,
          "(//h4[@class='ra-video-card__title'])["+str(number)+"]")
        assert txt.is_displayed(), \
            "for video section of 2019 Rising awards txt is not displayed on the Rising Awards page"
        print("txt header", txt.text)
        number += 1
    verify_bottom_section()


def verify_s_and_a_featured_articles():
    print("function called verify_s_and_a_featured_articles")
    header = driver.find_element(By.XPATH, "//h2[normalize-space()='S&A Featured Articles']")
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    assert header.is_displayed(), "header for 'S&A Featured Articles' is not displayed on the Rising Awards page"
    assert header.text is not None and header.text != "", \
        "'S&A Featured Articles' header is not present for Rising Awards page"
    grid = driver.find_element(By.XPATH, "//div[@class='ra-articles__grid d-grid']")
    assert grid.is_displayed(), "article grid for 'S&A Featured Articles' is not displayed on the Rising Awards page"
    article_heading = driver.find_elements_by_xpath(
      "//div[@class='ra-article-card d-flex flex-column ra-articles__card']")
    count = len(article_heading)
    number = 1
    while count >= number:
        time.sleep(1)
        temp_str = "(//div[@class='ra-article-card d-flex flex-column ra-articles__card']//a)["+str(number)+"]"
        article_link = driver.find_element(By.XPATH, temp_str)
        actions = ActionChains(driver)
        actions.move_to_element(article_link).perform()
        compare_2 = article_link.get_attribute("title")
        assert compare_2 is not None and compare_2 != "", "article title is not present"
        article_desc = driver.find_element(
          By.XPATH,
          "(//div[@class='ra-article-card d-flex flex-column ra-articles__card']/p)["+str(number)+"]")
        assert article_desc.text is not None and article_desc.text != "", "desc is not present for"+compare_2
        img = driver.find_element(By.XPATH, "(//div[@class='ra-article-card__image-wrapper']//img)["+str(number)+"]")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((
          By.XPATH, "(//div[@class='ra-article-card__image-wrapper']//img)["+str(number)+"]")))
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + compare_2

        article_link.click()
        # time.sleep(3)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.title_is(compare_2+" - SHADOW & ACT"))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, "for s&a featured articles, for one of the links"\
                                       + compare_2 + " ,title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("RISING Awards Digital 2021 - SHADOW & ACT"))
        time.sleep(1)
        number += 1
    back_to_top_button = driver.find_element(
      By.XPATH,
      "//button[@class='ra-btt__btn d-flex flex-column align-items-center mx-auto text-uppercase']")
    actions = ActionChains(driver)
    actions.move_to_element(back_to_top_button).perform()
    assert back_to_top_button.is_displayed(), "back to top button is not displayed"
    back_to_top_button.click()
    time.sleep(2)


def verify_footer():
    print("function called verify footer")
    footer = driver.find_element(
      By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()
    assert footer.is_displayed(), "footer is not displayed"


def verify_rising_awards_page_launch():
    print("function called verify_rising_awards_page_launch")
    link = driver.find_element(By.XPATH, "//a[normalize-space()='RISING AWARDS']")
    assert link.is_displayed(), "'RISING AWARDS' link is not displayed in the navigation bar"
    link.click()
    WebDriverWait(driver, 40).until(ec.title_is("RISING Awards Digital 2021 - SHADOW & ACT"))
    assert driver.title == \
           "RISING Awards Digital 2021 - SHADOW & ACT", "page title does not match for 'RISING AWARDS' page"
    verify_header_section()
    verify_categories_grid()
    verify_s_and_a_rising_awards()
    verify_s_and_a_featured_articles()
    verify_footer()


# environment()
# page_load()
# post_page_load_pop_up()
# verify_rising_awards_page_launch()
# verify_footer()
