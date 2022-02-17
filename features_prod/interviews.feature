Feature: Check Whether Interviews page for blavity Website ShadowAndAct.com is appropriate

  Scenario: To check whether Interviews page is as required
      Given the chrome browser is launched
      When I am on shadowandact page
      Then verify the application is launched successfully
      Then navigate to the Interviews page
      Then verify if all the article links are working as expected on the Interviews page
      Then verify for Interviews page, if the Load More stories button work as expected, also verify the links to the articles works as expected
      Then verify for Interviews page, if the Load More stories button work as expected (the second time when clicked), also verify initial link of the article, after clicking load more twice do work as expected
      Then verify footer section is present and displayed
      Then close the browser