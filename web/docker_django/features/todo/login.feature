Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      when we implement a test
      then behave will test it for us!

  Scenario: visit google and check
     Given the base url "http://google.com"
     When I visit "/"
     Then I should see "Google"