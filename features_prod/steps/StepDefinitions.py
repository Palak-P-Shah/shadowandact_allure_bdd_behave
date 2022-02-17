# import pytest
from behave import *
from common_pages import *
from Navigation_test import *
from rising_awards import *
from home_page_test import *
from podcast import verify_podcast
# from allure_commons.types import AttachmentType

# import allure
# from selenium import webdriver
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture(scope="function")
# def web_browser(request):
#     # Open browser:
#     b = webdriver.PhantomJS(executable_path='/tests/phantomjs')
#     b.set_window_size(1400, 1000)
#
#     # Return browser instance to test case:
#     yield b
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             b.execute_script("document.body.bgColor = 'white';")
#
#             allure.attach(b.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#         except:
#             pass # just ignore
#
#     # Close browser window:
#     b.quit()
#
#
# def after_step(context):
#     time.sleep(2)
#     if step.status == "failed":
#         allure.attach(context.browser.driver.get_screenshot_as_png(),
#                       name='screenshot',
#                       attachment_type=allure.attachment_type.PNG)
#


@given('the chrome browser is launched')
def step_impl(context):
    environment()


@given('url is launched')
def step_impl(context):
    environment()


@when('I am on shadowandact page')
def step_impl(context):
    page_load()


@then('verify the application is launched successfully')
def step_impl(context):
    post_page_load_pop_up()


@then('check whether page is loaded')
def step_impl(context):
    post_page_load_pop_up()


@then('verify whether navigation bar is present and displayed')
def step_impl(context):
    verify_nav_bar_presence()


@then('verify whether nav bar is present and displayed')
def step_impl(context):
    verify_nav_bar_presence()


@then('navigate to the Rising Awards page')
def step_impl(context):
    verify_rising_awards_page_launch()


@then('verify main image of Rising Awards page with 3 slide dots having relevant information regarding Rising Awards being displayed')
def step_impl(context):
    verify_header_section()


@then('verify on Rising Awards page, each tab of Behind The Scenes, Actors, Executives, Creators, Game-Changer having video , images and information provided')
def step_impl(context):
    verify_categories_grid()


@then('verify on Rising Awards page, S&A RISING AWARDS section having videos working with information provided')
def step_impl(context):
    verify_s_and_a_rising_awards()


@then('verify on Rising Awards page, S&A FEATURED ARTICLES section having images present and links working with information provided, and back to top button')
def step_impl(context):
    verify_s_and_a_featured_articles()


@then('verify links arrow buttons do work in carousel')
def step_impl(context):
    verify_carousel_articles_and_arrows()


@then('verify each article link, their details and arrow buttons do work as expected in carousel')
def step_impl(context):
    verify_carousel_articles_and_arrows()


@then('verify each article details and links for The Latest section')
def step_impl(context):
    verify_latest_section()


@then('verify number of articles before and after click of Load More Stories button in The Latest section, also verify the links to the articles works as expected')
def step_impl(context):
    verify_load_more_the_latest()
    verify_latest_section()


@then('verify number of articles before and after click of Load More Stories button(the second time when clicked) in The Latest section, also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_load_more_the_latest()
    verify_load_more_the_latest()
    verify_latest_section()


@then('verify latest section')
def step_impl(context):
    verify_latest_section()


@then('verify podcast links and check whether sample podcast is working')
def step_impl(context):
    verify_podcast()


@then('verify side bar top article section')
def step_impl(context):
    verify_top_articles()


@then('verify side bar sign up section')
def step_impl(context):
    verify_signup()


@then('verify side bar most popular section')
def step_impl(context):
    verify_most_popular()


@then('verify each article of side bar most popular section')
def step_impl(context):
    verify_most_popular()


@then('verify shadowandact originals section')
def step_impl(context):
    verify_shadow_and_act_originals()


@then('verify pre and post click see more originals button count comparison of articles under shadowandact originals')
def step_impl(context):
    verify_post_click_more_originals_number_comparison()


@then('verify other trending black news section')
def step_impl(context):
    verify_other_trending_black_news()


@then('verify whether all nav bar links are working')
def step_impl(context):
    verify_nav_bar_links()


@then('verify footer section is present and displayed')
def step_impl(context):
    verify_footer_presence()


@then('verify footer links are working as expected')
def step_impl(context):
    verify_footer_links()


@then('navigate to the Film page')
def step_impl(context):
    verify_particular_page("FILM")


@then('navigate to the Television page')
def step_impl(context):
    verify_particular_page("TELEVISION")


@then('verify if all the article links are working as expected on the Television page')
def step_impl(context):
    verify_each_article("TELEVISION", "Television")


@then('verify for Television page, if the Load More stories button work as expected, also verify the links to the articles works as expected')
def step_impl(context):
    verify_number_of_articles("Television")
    verify_each_article("TELEVISION", "Television")


@then('verify for Television page, if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_number_of_articles("Television")
    verify_number_of_articles("Television")
    verify_each_article("TELEVISION", "Television")


@then('navigate to the Web Series page')
def step_impl(context):
    verify_particular_page("WEB SERIES")


@then('verify if all the article links are working as expected on the Web Series page')
def step_impl(context):
    verify_each_article("WEB SERIES", "Web Series")


@then('verify for Web Series page, if the Load More stories button work as expected, also verify the links to the articles works as expected')
def step_impl(context):
    verify_number_of_articles("Web Series")
    verify_each_article("WEB SERIES", "Web Series")


@then('verify for Web Series page, if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_number_of_articles("Web Series")
    verify_number_of_articles("Web Series")
    verify_each_article("WEB SERIES", "Web Series")


@then('navigate to the Interviews page')
def step_impl(context):
    verify_particular_page("INTERVIEWS")


@then('verify if all the article links are working as expected on the Interviews page')
def step_impl(context):
    verify_each_article("INTERVIEWS", "Interviews")


@then('verify for Interviews page, if the Load More stories button work as expected, also verify the links to the articles works as expected')
def step_impl(context):
    verify_number_of_articles("Interviews")
    verify_each_article("INTERVIEWS", "Interviews")


@then('verify for Interviews page, if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_number_of_articles("Interviews")
    verify_number_of_articles("Interviews")
    verify_each_article("INTERVIEWS", "Interviews")



@then('verify if all the article links are working as expected on the Film page')
def step_impl(context):
    verify_each_article("FILM", "Film")


@then('verify if the Load More stories button work as expected, also verify the links to the articles works as expected')
def step_impl(context):
    verify_number_of_articles("Film")
    verify_each_article("FILM", "Film")


@then('verify if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected')
def step_impl(context):
    verify_number_of_articles("Film")
    verify_number_of_articles("Film")
    verify_each_article("FILM", "Film")


@then('verify whether Film page is as required')
def step_impl(context):
    verify_particular_page("FILM")


@then('verify whether Interviews page is as required')
def step_impl(context):
    verify_particular_page("INTERVIEWS")


@then('verify whether Television page is as required')
def step_impl(context):
    verify_particular_page("TELEVISION")


@then('verify whether Web Series page is as required')
def step_impl(context):
    verify_particular_page("WEB SERIES")


@then('close the browser')
def step_impl(context):
    driver.quit()
