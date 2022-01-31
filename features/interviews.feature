Feature: Check Whether interviews page for blavity Website ShadowAndAct.com is appropriate

  Scenario: To check whether Interviews page is as required
      Given url is launched
      When I am on shadowandact page
      Then check whether page is loaded
      Then verify whether Interviews page is as required
      Then verify footer section is present and displayed
      Then close the browser