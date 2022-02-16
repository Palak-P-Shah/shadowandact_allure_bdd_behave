Feature: Home Page Verification for staging.ShadowAndAct.com for latest and sign up sections
 
  Scenario: Verify the different sections of the Home Page for website staging.ShadowAndAct.com for latest and sign up sections
    Given the chrome browser is launched
    When I am on shadowandact page
    Then verify the application is launched successfully
    Then verify each article details and links for The Latest section
    Then verify number of articles before and after click of Load More Stories button in The Latest section, also verify the links to the articles works as expected
    Then verify number of articles before and after click of Load More Stories button(the second time when clicked) in The Latest section, also verify initial link of the article, after clicking load more twice do work as expected
    # Then verify side bar top article section
    Then verify side bar sign up section
    Then close the browser