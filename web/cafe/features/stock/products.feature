Feature: Products
  In order to later manage stock of products
  As a user
  I want to create and view products

    Background:
        Given a browser
        And I am logged in as "admin"

    Scenario: I should see created products
        When I visit "/products"
        Then I should see "Fanta"
        And I should see "Cola"

    Scenario: I should be able to create products
        When I visit "/products"
        And I select by text "Soda" from "group_id"
        And I fill in "name" with "Dr Pepper"
        And I fill in "price" with "25"
        And I fill in "price_rent" with "0"
        And I click "Create Product"
        Then I should see "Dr Pepper"

    Scenario: I should be able to update product stock count
        When I visit "/products"
        And I fill in "10" for "Fanta" stock
        And I click "Update Stock" for "Fanta"
        Then "Fanata" stock should be "10"
