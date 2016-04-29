Feature: Home page
  In order to use the app
  As a user
  I want to see the homepage

    Background:
        Given a browser

    Scenario: I should see the home page
        When I visit "/"
        Then the browser's URL should be "/"
        And I should see "Stock System"

