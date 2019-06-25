Feature: Recommendation with fridge
  Recommending recipes that maximize the usage of user's fridge

  Scenario: Recommend recipes with ingredients in the user's fridge
    Given a user with id: 675719
    When The user want recommended recipes that have ingredients in his fridge
    Then a list of recipes that privilege the user's fridge is returned
    And the first recommended recipe has more fridge ingredients than the second


  Scenario: Recommend recipes with ingredients in the host's fridge for a group of users
    Given a group of users with id: 675719, 1654092, 77852
    When the host wants recommended recipes for its group
    Then a list of recipes that privilege the host's fridge is returned
    And the first recommended recipe has more ingredients from the fridge than the second