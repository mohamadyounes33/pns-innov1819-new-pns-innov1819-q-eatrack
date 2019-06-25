Feature: Recommendation with preferences
  Recommending recipes that respect the user's preferences

  Scenario: Recommend recipes with preferred ingredients of a user    #55
    Given a user with id 675719
    When The user want recommended recipes that respect his preferences
    Then a list of recipes that privilege the user's preferences is returned
    And the first recommended recipe has more preferred ingredients than the second

  Scenario: don't recommend recipes that contain ingredients disliked or allergic for the user
    Given a user with id 8632557
    When The user want recommended recipes that respect his preferences
    Then a list of recipes that don't contain disliked/allergic ingredients is returned

  Scenario: Recommend recipes with preferred ingredients of a group of users  #56
    Given a group of users with id: 2419700, 1654092, 77852
    When the host wants  recommended recipes for its group
    Then a list of recipes that privilege preferences of all users of the group is returned

  Scenario: don't recommend recipes that contain ingredients disliked or allergic for any member of the group
    Given a group of users with id: 2419700, 1654092, 77852
    When the host wants  recommended recipes for its group
    Then a list of recipes that don't contain disliked/allergic ingredients for any member of the group is returned