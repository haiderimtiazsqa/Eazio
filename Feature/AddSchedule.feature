
Feature: User Schedule Management

  Background: Successful login with valid credentials
    Given the user is on the login page
    When the user enters the username and password
    And the user clicks the login button
    Then the user should be redirected to the dashboard


  Scenario: Add a new schedule
    Given the user clicks on the schedule tab
    And the user clicks the add schedule button
    When the user enters the schedule name
    And the user enters the schedule description
    And the user selects the timings
    And the user selects the schedule days
    Then the user clicks on the add button
    And the user should see a success message "Schedule added successfully."