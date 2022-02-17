from environment import *


def verify_podcast():
    print("in the function verify_podcast")
    podcast = driver.find_element(By.XPATH, "//a[normalize-space()='PODCAST']")
    actions = ActionChains(driver)
    actions.move_to_element(podcast).perform()
    assert podcast.is_displayed(), "'PODCAST' heading is not displayed"
    podcast.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(ec.title_is("Opening Act Podcast"))
    assert "Opening Act Podcast" in driver.title, "title of podcast website does not match"
    time.sleep(2)
    # WebDriverWait(driver, 10).until(ec.presence_of_element_located((
    #   By.CSS_SELECTOR, "(//img[@class='summary-thumbnail-image loaded'])[1]"
    # )))
    listen_to_podcast = driver.find_element(By.XPATH, "//div[@class='sqs-block-button-container--left']//a")
    actions = ActionChains(driver)
    actions.move_to_element(listen_to_podcast).perform()
    listen_to_podcast.click()
    driver.switch_to.window(driver.window_handles[2])
    WebDriverWait(driver, 10).until(ec.title_contains("Blog"))
    assert "Blog" in driver.title, "Title text does not contain Blog"
    time.sleep(2)
    fixed_podcast = driver.find_element(
      By.XPATH,
      "//img[@alt='Episode 25 - Brandy']")
    actions = ActionChains(driver)
    actions.move_to_element(fixed_podcast).perform()
    assert fixed_podcast.is_displayed(), "'Listen To Podcast' heading is not displayed"
    text = driver.find_element(By.XPATH, "(//div[@class='blog-basic-grid--text']//h1//a)[1]")
    tmp_text = text.text
    fixed_podcast.click()
    # time.sleep(7)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
      By.XPATH, "//div[@class='blog-item-top-wrapper']//div//h1"
    )))
    player = driver.find_element(By.XPATH, "(//div[@class='sqs-block-content']//iframe)[1]")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
      By.XPATH, "(//div[@class='sqs-block-content']//iframe)[1]"
    )))
    driver.execute_script("arguments[0].scrollIntoView();", player)
    frame = driver.find_element(By.XPATH, "(//div[@class='sqs-block-content']//iframe)[1]")
    driver.switch_to.frame(frame)
    # time.sleep(5)
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//span[@class='player-grid__play']"
    )))
    play = driver.find_element(By.XPATH, "//span[@class='player-grid__play']")
    # actions = ActionChains(driver)
    # actions.move_to_element(play).perform()
    play.click()
