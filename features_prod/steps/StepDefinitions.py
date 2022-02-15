# import pytest
from behave import *
from common_pages import *
from Navigation_test import *
from rising_awards import *
from home_page_test import *

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


@given('url is launched')
def step_impl(context):
    environment()


@when('I am on shadowandact page')
def step_impl(context):
    page_load()


@then('check whether page is loaded')
def step_impl(context):
    post_page_load_pop_up()


@then('verify whether nav bar is present and displayed')
def step_impl(context):
    verify_nav_bar_presence()


@then('verify whether Rising Awards page is as required')
def step_impl(context):
    verify_rising_awards_page_launch()


@then('verify links arrow buttons do work in carousel')
def step_impl(context):
    verify_carousel_articles_and_arrows()


@then('verify latest section')
def step_impl(context):
    verify_latest_section()


@then('verify side bar top article section')
def step_impl(context):
    verify_top_articles()


@then('verify side bar sign up section')
def step_impl(context):
    verify_signup()


@then('verify side bar most popular section')
def step_impl(context):
    verify_most_popular()


@then('verify shadowandact originals section')
def step_impl(context):
    verify_shadow_and_act_originals()


@then('verify post click count comparison under shadowandact originals')
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
