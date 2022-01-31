Feature: Home Page Verification for ShadowAndAct.com for originals , count comaprison and other trending
 
  Scenario: Verify the different sections of the Home Page for ShadowAndAct.com for originals , count comaprison and other trending
    Given url is launched
    When I am on shadowandact page
    Then check whether page is loaded
    Then verify shadowandact originals section
    Then verify post click count comparison under shadowandact originals
    Then verify other trending black news section
    Then close the browser