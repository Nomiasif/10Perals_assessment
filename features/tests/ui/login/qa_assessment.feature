Feature: Verify Login Functionality of Swag Labs
    As a QE
    I want to automate login cases of Swag Labs
    So that I may complete my 10Pearls assessment

    Background: Available on Login Page
      #To run these scenarios on Microsoft Edge, just replace "Chrome" with "Edge" in the below statement
       Given user is on Swag Labs Login Page on "Chrome" browser

    @10pearls
    Scenario: Verify login with valid username and password - Standard User
      When user logins with credentials from config file
      And user clicks on Login button
      Then user should see "Products" content on the page

    @10pearls
    Scenario: Verify login with valid username and password - Locked Out User
      When user logins with "locked_out_user" username
      And user clicks on Login button
      Then user should see "Epic sadface: Sorry, this user has been locked out." validation message on the page

    @10pearls
    Scenario: Verify login with valid username and password - Problem User
      When user logins with "problem_user" username
      And user clicks on Login button
      Then user should see "Products" content on the page

    @10pearls
    Scenario: Verify login with valid username and password - Performance Glitch User
      When user logins with "performance_glitch_user" username
      And user clicks on Login button
      Then user should see "Products" content on the page

    @10pearls
    Scenario: Verify login with invalid username
      When user logins with "wrong" username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with invalid password
      When user logins with "wrong" password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with invalid username and password
      When user logins with "wrong" username and "wrong" password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login without username
      When user logins without username
      And user clicks on Login button
      Then user should see "Epic sadface: Username is required" validation message on the page

    @10pearls
    Scenario: Verify login without password
      When user logins without password
      And user clicks on Login button
      Then user should see "Epic sadface: Password is required" validation message on the page

    @10pearls
    Scenario: Verify login without username and password
      When user logins without username and password
      And user clicks on Login button
      Then user should see "Epic sadface: Username is required" validation message on the page

    @10pearls
    Scenario: Verify login with only spaces in username field
      When user logins with "  " username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with only spaces in password field
      When user logins with "  " password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with only spaces in username and password fields
      When user logins with only spaces in username and password fields
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with leading spaces in username field
      When user logins with "  standard_user" username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with trailing spaces in username field
      When user logins with "standard_user  " username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with leading and trailing spaces in username field
      When user logins with "  standard_user  " username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with leading spaces in password field
      When user logins with "  secret_sauce" password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with trailing spaces in password field
      When user logins with "secret_sauce  " password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with leading and trailing spaces in password field
      When user logins with "  secret_sauce  " password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with username in all caps
      When user logins with "STANDARD_USER" username
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify login with password in all caps
      When user logins with "SECRET_SAUCE" password
      And user clicks on Login button
      Then user should see "Epic sadface: Username and password do not match any user in this service" validation message on the page

    @10pearls
    Scenario: Verify logout functionality
      When user logins with credentials from config file
      And user clicks on Login button
      And user clicks on Logout link
      Then user should see "Accepted usernames are:" content on the page

    @10pearls
    Scenario: Verify refreshing of credentials fields when page gets refreshed
      When user logins with credentials from config file
      And user refreshes the page
      Then user should see empty username and password fields

