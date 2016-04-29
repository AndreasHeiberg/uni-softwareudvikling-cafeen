Feature: Users can login
  In order to use the app
  As a user
  I want to login

    Background:
        Given a browser

    Scenario: I should be redirected to the login form initially
        When I visit "/"
        Then the browser's URL should be "/accounts/login/?next=/"

    Scenario: I should be redirected back to the page I tried to access after login
        When I visit "/products"
        Then the browser's URL should be "/accounts/login/?next=/products"
        And I fill in "username" with "admin"
        And I fill in "password" with "admin-password"
        And I click "login"
        Then the browser's URL should be "/products"
        And I should see "Products"

    Scenario: I should see an error if I didn't provide the right details
        When I visit "/"
        Then the browser's URL should be "/accounts/login/?next=/"
        And I fill in "username" with "admin"
        And I fill in "password" with "wrong-password"
        And I click "login"
        Then the browser's URL should be "/accounts/login/"
        And I should see "Your username and password didn't match."
