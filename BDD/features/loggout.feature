Feature: Loggout

  Scenario: A logged in user wants to log out (LO)

        Given User is logged in SGME
        When User tries to log out by using the respective button
        Then SGME platform redirects the user to the log in page