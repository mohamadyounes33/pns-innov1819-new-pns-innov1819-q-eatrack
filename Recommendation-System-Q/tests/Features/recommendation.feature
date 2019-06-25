# Created by Mohamed Younes at 5/30/2019
Feature: Recipe Recommendation

  Scenario: Single User Recommendation
    Given a user with id 2419700
    When the user wants recommended recipes
    Then The recommendation system returns a list of recipes that matches the user's history and preferences


  Scenario: Group of users Recommendation
    Given a group of users with ids: 2419700, 1654092, 77852
    When the host wants recommended recipes for its group
    Then the recommendation system returns a list of recipes that matches all user's history and preferences


  Scenario: Recommendation after updating preferences (adding preferences)   # 30
    Given a user with id 869094
    When he adds preferences : walnut,cake,rum,egg,water,vegetable oil,vanilla,Glaze,butter,water,white sugar,rum
    And he asks for recommendation
    Then the first recommended recipe has in ingredients : walnut,cake,rum,egg,water,vegetable oil,vanilla,Glaze,butter,water,white sugar,rum



  Scenario: Recommendation after updating preferences (removing preferences)  # 26
    Given a user with id 1478626
    When he asks for recommendation firstly
    And he removes preferences : olive, egg, baking powder
    And he asks for recommendation
    Then the first recommendation's first recipe has olive, egg, baking powder, the second recommendation's first recipe hasnt