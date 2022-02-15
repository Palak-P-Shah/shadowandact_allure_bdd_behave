Feature: Home Page Verification for staging.ShadowAndAct.com for navbar carousel and most popular
 
  Scenario: Verify the different sections of the Home Page for staging.ShadowAndAct.com for navbar carousel and most popular
    Given url is launched
    When I am on shadowandact page
    Then check whether page is loaded
    Then verify whether nav bar is present and displayed
    Then verify links arrow buttons do work in carousel
    Then verify side bar most popular section
    Then close the browser