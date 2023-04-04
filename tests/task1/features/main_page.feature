Feature: Verifying the main page url opens the correct page

  Scenario: The main page should have correct url
    Given I open main page
    Then the url should be "https://automationexercise.com/"

  Scenario: The main page should have correct title
    Given I open main page
    Then the title should be "Automation Exercise"