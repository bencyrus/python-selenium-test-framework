Feature: Shopping Cart

  Scenario: Login with invalid credentials
    Given I am on the login page
    When I execute login with "invalidemail@test.com" as email and "invalid_password" as password
    Then I should see a login failed message

  Scenario: Login with valid credentials
    Given I am on the login page
    When I execute login with "mahdi.mohaghegh2001@gmail.com" as email and "12345678" as password
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
    When I add the product number 2 to the cart
    Then I should be able to view the cart

  Scenario: Remove 1 T-shirt from the cart and proceed to checkout
    Given I am on the shopping cart page
    And The cart is not empty
    When I remove the product number 1 from the cart
    Then I should be able to proceed to checkout
    Then I should be able to place the order

  Scenario: Pay with a credit card
    Given I am on the payment page
    When I enter the credit card information with the following details
      | field       | value            |
      | card holder | Ben Cyrus        |
      | card number | 4242424242424242 |
      | cvv         | 123              |
      | expiry month| 12               |
      | expiry year | 2026             |
    Then I should be able to confirm and pay the order
    When I see order confirmation message
    Then I should be able to download the invoice

