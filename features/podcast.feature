Feature: Check Whether sample podcast for blavity Website staging.ShadowAndAct.com is appropriate

  Scenario: To check sample podcast on staging.shadowandact.com
      Given the chrome browser is launched
      When I am on shadowandact page
      Then verify the application is launched successfully
      Then verify podcast links and check whether sample podcast is working
      Then close the browser