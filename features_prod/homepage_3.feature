Feature: Home Page Verification for ShadowAndAct.com for originals , count comaprison and other trending
 
  Scenario: Verify the different sections of the Home Page for ShadowAndAct.com for originals , count comaprison and other trending
    Given the chrome browser is launched
    When I am on shadowandact page
    Then verify the application is launched successfully
    Then verify shadowandact originals section
    Then verify pre and post click see more originals button count comparison of articles under shadowandact originals
    Then verify other trending black news section
    Then close the browser