Feature: Access Permissions

      Scenario: A user, logged in SGME, wants to go to permissions webpage

        Given User is logged in SGME and is currently on SGME webpage
        When User clicks on permission tag in sidebar
        Then SGME platform redirects the user to the permissions page