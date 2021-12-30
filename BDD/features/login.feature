Feature: Login

      Scenario: Valid Login (1a)

        Given a user is in the SGME platform login page
        When the user insert his valid credentials
        Then SGME platform redirects the user to the home page


      Scenario: Invalid Login (1b)

        Given a user is in the SGME platform login page#2
        When the user insert his invalid credentials
        Then SGME platform returns that the credentials are not valid
