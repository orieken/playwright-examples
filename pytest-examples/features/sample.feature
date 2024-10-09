Feature: Visiting playwright.dev

  Scenario: Visiting the Playwright website
    Given I am on the Playwright website
    Then I should see "Playwright" in the title

  Scenario: Go to Getting Started
    Given I am on the Playwright website
    When I click on "Getting Started"
    Then I should see "Getting Started" in the title
    And the Heading should be "Installation"
