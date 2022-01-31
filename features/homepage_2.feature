Feature: Home Page Verification for ShadowAndAct.com for latest and sign up section
 
  Scenario: Verify the different sections of the Home Page for ShadowAndAct.com for latest and sign up section
    Given url is launched
    When I am on shadowandact page
    Then check whether page is loaded
    Then verify latest section
    # Then verify side bar top article section
    Then verify side bar sign up section
    Then close the browser