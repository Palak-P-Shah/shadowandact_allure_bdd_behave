Feature: Check Whether rising awards page for blavity Website ShadowAndAct.com is appropriate

  Scenario: To check whether Rising Awards page is as required
      Given the chrome browser is launched
      When I am on shadowandact page
      Then verify the application is launched successfully
      Then navigate to the Rising Awards page
      Then verify main image of Rising Awards page with 3 slide dots having relevant information regarding Rising Awards being displayed
      Then verify on Rising Awards page, each tab of Behind The Scenes, Actors, Executives, Creators, Game-Changer having video , images and information provided
      Then verify on Rising Awards page, S&A RISING AWARDS section having videos working with information provided
      Then verify on Rising Awards page, S&A FEATURED ARTICLES section having images present and links working with information provided, and back to top button
      Then verify footer section is present and displayed
      Then close the browser