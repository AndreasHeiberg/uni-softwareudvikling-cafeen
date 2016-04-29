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

    Scenario: I should be able to go to Product Groups
        When I visit "/"
        Then I should see "Product Groups"

    Scenario: I should be able to go to Products
        When I visit "/"
        Then I should see "Products"
