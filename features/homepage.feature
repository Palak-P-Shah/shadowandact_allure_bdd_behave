Feature: Home Page Verification for staging.ShadowAndAct.com for navigation links, carousel and most popular sections
 
  Scenario: Verify the different sections of the Home Page for staging.ShadowAndAct.com for navigation links, carousel and most popular sections
     Given the chrome browser is launched
     When I am on shadowandact page
     Then verify the application is launched successfully
     Then verify whether navigation bar is present and displayed
     Then verify each article link, their details and arrow buttons do work as expected in carousel
     Then verify each article of side bar most popular section
     Then close the browser