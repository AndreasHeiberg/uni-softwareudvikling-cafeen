Feature: Product Groups
  In order to group products meaninfully
  As a user
  I want to create product groups

    Background:
        Given a browser

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
