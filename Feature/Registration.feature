Feature: User Registration

  Background: User registers on the registration page
    Given the user is on the registration page
    When the user enters the First Name
    And the user enters the Last Name
    And the user enters the Username
    And the user enters the Email
    And the user enters the Password
    And the user enters the Confirm Password
    And the user clicks the next button
    Then the user should be taken to the next step of registration



  Scenario: User completes business information after registration
    When the user clicks the get start button
    Then the user is redirected to the business information form
    When the user enters the business name
    And the user selects the business category
    And the user selects the business type
    And the user enters the phone number
    And the user enters the website
    And the user enters the address
    And the user selects the country
    And the user selects the city
    And the user clicks the verify button
    And the user enters the OTP






