Feature: Shopping Cart

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I execute login with invalidemail@test.com as email and invalid_password as password
    Then I should see a login failed message

  Scenario: Login with valid credentials
    Given I am on the login page
    When I execute login with mahdi.mohaghegh2001@gmail.com as email and 12345678 as password
    Then I should be redirected to the main page with the title Automation
    And I should see the logout button
    And the user name should be Ben Cyrus

  Scenario: Select 2 T-Shirts and add to cart
    Given I am on the main page
    And I am logged in successfully with the user name Ben Cyrus
    When I open the products page
    Then I should see the All Products title
    When I search for tshirts
    Then I should see the Searched Products title
    When I add the product number 1 to the cart
    Then I should see a modal confirming the addition to cart
    And I should be able to continue shopping
    When I add the product number 2 to the cart
    Then I should see a modal confirming the addition to cart
    And I should be able to view the cart
