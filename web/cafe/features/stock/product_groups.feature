Feature: Product Groups
  In order to group products meaninfully
  As a user
  I want to create product groups

    Background:
        Given a browser
        And I am logged in as "admin"

    Scenario: I can create product groups as an admin
        Given I am logged in as "admin"
        When I visit "/product-groups"
        Then I should see button "Create Product Group"

    Scenario: I can't create product groups as a non-admin
        Given I am logged in as "key-carrier"
        When I visit "/product-groups"
        Then I should not see button "Create Product Group"
        When I POST to "/products" with:
            |key        |value|
            |name       |Food |
        Then I should a permission denied response

    Scenario: I should see created groups
        When I visit "/product-groups"
        Then I should see "Soda"
        And I should see "Beer"
        And I should see "Snacks"

    Scenario: I should be able to create groups
        When I visit "/product-groups"
        And I fill in "name" with "Wine"
        And I click "Create Product Group"
        Then I should see "Wine"

    Scenario: I can access the product group section of the app
        Given I am logged in as "admin"
        When I visit "/product-groups"
        Then I should see button "Create Product Group"
        And I should not see "You don't have permission."

    Scenario: I can't access the product group section as a non admin
        Given I am logged in as "key-carrier"
        When I visit "/product-groups"
        Then I should not see button "Create Product Group"
        And I should see "You don't have permission."
