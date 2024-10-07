Feature: Admin Add Employee

  Background: Successful login with valid credentials
    Given the user is on the login page
    When the user enters the username and password
    And the user clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Admin adds a new employee
#    Given the admin is on the dashboard
    When the admin clicks on the People tab from the sidebar
    Then the admin should be redirected to the People Insight page
    When the admin clicks on the Employee tab
    When the admin clicks on the Add Employee button
    Then the admin should be redirected to the Add Employee form
    When the admin enters the employee's first name
    And the admin enters the employee's last name
    And the admin enters the employee's email address
    And the admin enters the employee's mobile number
    And the admin selects the reporting manager
    And the admin selects the country
    And the admin selects the state
    And the admin clicks on the Add Employee from button
    Then the admin should be redirected to the Employee Listing page