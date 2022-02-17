Feature: Check Whether navigation links for shadowandact Website shadowandact.com is appropriate

  Scenario: To check whether all navigation bar links are as required
      Given the chrome browser is launched
      When I am on shadowandact page
      Then verify the application is launched successfully
      Then verify whether nav bar is present and displayed
      Then verify whether all nav bar links are working
      Then verify footer section is present and displayed
      Then verify footer links are working as expected
      Then close the browser