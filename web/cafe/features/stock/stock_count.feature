Feature: Stock Count
  In order to keep track of stock between shifts
  As a user
  I want to count stock before and after my shift

    Background:
        Given a browser
        And I am logged in as "key-carrier"

    Scenario: I should see the products to count before shift
        When I visit "/products/count?time=pre-shift"
        Then I should see "Fanta"
        And I should see "Cola"
        And I should see "Dr Pepper"

    Scenario: I should see the products to count after shift
        When I visit "/products/count?time=post-shift"
        Then I should see "Fanta"
        And I should see "Cola"
        And I should see "Dr Pepper"

    Scenario: I should be able to update stock before shift
        When I visit "/products/count?time=pre-shift"
        And I fill in "10" for "Fanta" stock
        And I fill in "10" for "Cola" stock
        And I click "Save count"
        And I visit "/products"
        Then "Fanata" stock should be "10"
        And "Cola" stock should be "10"

    Scenario: I should be able to update stock before shift
        When I visit "/products/count?time=pre-shift"
        And I fill in "10" for "Fanta" stock
        And I fill in "10" for "Cola" stock
        And I click "Save count"
        And I visit "/products"
        Then "Fanata" stock should be "10"
        And "Cola" stock should be "10"

    Scenario: I should get shift turn over after my shift
        When I visit "/products/count?time=post-shift"
        And I fill in "10" for "Fanta" stock
        And I fill in "10" for "Cola" stock
        And I click "Save count"
        Then I should see "Turn over this shift: 500DKK"

    Scenario: I should get alerted if stock doesn't match last count before my shift
        When I visit "/products/count?time=pre-shift"
        And I fill in "10" for "Fanta" stock
        And I fill in "10" for "Cola" stock
        And I click "Save count"
        Then I should see "At last stock count at the start of the shift there was an inconsistency with the last stock count. Be adviced:"

    Scenario: The admin should get alerted if stock doesn't match last count before my shift
        When I visit "/products/count?time=pre-shift"
        And I fill in "10" for "Fanta" stock
        And I fill in "10" for "Cola" stock
        And I click "Save count"
        Then an email should be sent to "admin" user
