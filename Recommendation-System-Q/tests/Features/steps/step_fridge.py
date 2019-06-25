from behave import *

from src.group_recommender import *


@when("The user want recommended recipes that have ingredients in his fridge")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.recommendations = aggregated_voting([context.user], True)
    print(context.recommendations)
    # get the user's fridge from the server
    context.fridge = User(context.user).get_fridge()


@then("a list of recipes that privilege the user's fridge is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert any(
        ingredient in context.recommendations[0]['Ingredients'] for ingredient in context.fridge)


@step("the first recommended recipe has more fridge ingredients than the second")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    first_recipe = context.recommendations[0]
    second_recipe = context.recommendations[1]
    fridge = context.fridge
    assert contains_ingredient_nbr(first_recipe["RecipeID"], fridge) >= contains_ingredient_nbr(
        second_recipe["RecipeID"], fridge)



@then("a list of recipes that privilege the host's fridge is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.fridge:
        assert any(
            ingredient in context.group_recommendation[0]['Ingredients'] for ingredient in context.fridge)


@step("the first recommended recipe has more ingredients from the fridge than the second")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    first_recipe = context.group_recommendation[0]
    second_recipe = context.group_recommendation[1]
    fridge = context.fridge
    assert contains_ingredient_nbr(first_recipe["RecipeID"], fridge) >= contains_ingredient_nbr(
        second_recipe["RecipeID"], fridge)
