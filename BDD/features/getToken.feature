Feature: Get Authorized via Token

      Scenario: A user with valid credentials is trying to get authorized by his token
        Given User is logged in SGME and is currently on documentation webpage
        When User use it's credentials to get their respective token and apply for the authorization
        Then SGME platform informs that the authorization process was successful


