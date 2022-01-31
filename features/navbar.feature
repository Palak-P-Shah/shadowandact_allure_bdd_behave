Feature: Check Whether navigation links for shadowandact Website staging.shadowandact.com is appropriate

  Scenario: To check whether nav bar links are as required
      Given url is launched
      When I am on shadowandact page
      Then check whether page is loaded
      Then verify whether nav bar is present and displayed
      Then verify whether all nav bar links are working
      Then verify footer section is present and displayed
      Then verify footer links are working as expected
      Then close the browser