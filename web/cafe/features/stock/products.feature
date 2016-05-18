Feature: Products
  In order to later manage stock of products
  As a user
  I want to create and view products

    Background:
        Given a browser
        And I am logged in as "admin"

    Scenario: I can create products as an admin
        Given I am logged in as "admin"
        When I visit "/products"
        Then I should see button "Create Product"

    Scenario: I can't create products as a non-admin
        Given I am logged in as "key-carrier"
        When I visit "/products"
        Then I should not see button "Create Product"
        When I POST to "/products" with:
            | name       | Cider |
            | group_id   | 1     |
            | price      | 25    |
            | price_rent | 0     |
        Then I should a permission denied response

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

    Scenario: I can't update products stock as a non-admin
        Given I am logged in as "key-carrier"
        When I visit "/products"
        Then I should not see button "Update Stock"
        When I PUT to "/products/1" with:
            |key   |value|
            |stock |25   |
        Then I should a permission denied response
