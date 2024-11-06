Feature: Admin create feeds

   Background: Successful login with valid credentials
    Given the user is on the login page
    When the user enters the username and password
    And the user clicks the login button
    Then the user should be redirected to the dashboard


 Scenario: Admin creates a feed
    When the admin navigates to the "Feeds" section
    And the admin clicks on "Create Feed"
    And the admin enters the feed content
    And the admin clicks the "Post" button
   And the admin clicks on "Like" for the newly created feed
   And  the admin write comment on feed
   And the admin redirect to all event
   And the admin click on add event button
   And admin add the event


