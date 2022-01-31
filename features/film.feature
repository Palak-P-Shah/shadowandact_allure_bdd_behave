Feature: Check Whether film page for blavity Website ShadowAndAct.com is appropriate

  Scenario: To check whether Film page is as required
      Given url is launched
      When I am on shadowandact page
      Then check whether page is loaded
      Then verify whether Film page is as required
      Then verify footer section is present and displayed
      Then close the browser