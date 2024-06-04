Feature: Test the functionality of the login page
  # Scenariu 1: email neinregistrat + o parola oarecare
  # Scenariu 2: fara email + o parola oarecare
  # Scenariu 3: invalid email + o parola oarecare

  Scenario: Check that "No customer account found" error message is displayed when user tries to login whit unregistered email
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I insert a password
    And I click the login button
    Then Main error is displayed

#  Scenario: Check that "Please enter your email" error message is displayed when user tries to login without providing an email address
#    Given I am on the login page
#    When I insert " " email
#    And I insert a password
#    And I click the login button
#    Then Email error is displayed
#    And Email error message contains "Please enter your email"
#
#    Scenario: Check that "Wrong enter your email" error message is displayed when user tries to login with invalid format email
#    Given I am on the login page
#    When I insert "format invalid" email
#    And I insert a password
#    And I click the login button
#    Then Email error is displayed
#    And Email error message contains "Wrong email"

