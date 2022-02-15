Feature: Home Page Verification for ShadowAndAct.com for most popular section
 
  Scenario: Verify the different most polular section of the Home Page for ShadowAndAct.com
    Given url is launched
    When I am on shadowandact page
    Then check whether page is loaded
    Then verify whether nav bar is present and displayed
    Then verify side bar most popular section
    Then close the browser