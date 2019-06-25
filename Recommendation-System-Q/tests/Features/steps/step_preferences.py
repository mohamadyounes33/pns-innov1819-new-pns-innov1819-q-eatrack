from behave import *

from src.group_recommender import *


@given("a user with id: {id_number:d}")
def step_impl(context, id_number):
    """
    :type context: behave.runner.Context
    """
    context.user = id_number
    context.preference = User(id_number).get_preferences()


@when("The user want recommended recipes that respect his preferences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.recommendations = aggregated_voting([context.user])


@then("a list of recipes that privilege the user's preferences is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert any(
        ingredient in context.recommendations[0]['Ingredients'] for ingredient in User(context.user).get_preferences())


@then("a list of recipes that don't contain disliked/allergic ingredients is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert not any(
        ingredient in context.recommendations[0]['Ingredients'] for ingredient in User(context.user).get_allergies())


@given("a group of users with id: {user1_id:d}, {user2_id:d}, {user3_id:d}")
def step_impl(context, user1_id, user2_id, user3_id):
    """
    :type context: behave.runner.Context
    """
    context.user1 = user1_id
    context.user2 = user2_id
    context.user3 = user3_id
    context.groupe = [context.user1, context.user2, context.user3]


@when("the host wants  recommended recipes for its group")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.group_recommendation = aggregated_voting(context.groupe)


@then("a list of recipes that privilege preferences of all users of the group is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert any(
        ingredient in context.group_recommendation[0]['Ingredients'] for ingredient in
        list(union_group_preferences(idToUser(context.groupe)).keys()))


@then("a list of recipes that don't contain disliked/allergic ingredients for any member of the group is returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert not any(
        ingredient in context.group_recommendation[0]['Ingredients'] for ingredient in
        union_group_undesirable(idToUser(context.groupe)))


@step("the first recommended recipe has more preferred ingredients than the second")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    first_recipe = context.recommendations[0]
    second_recipe = context.recommendations[1]
    preferences = User(context.user).get_preferences()
    assert contains_ingredient_nbr(first_recipe["RecipeID"], preferences) >= contains_ingredient_nbr(
        second_recipe["RecipeID"], preferences)
