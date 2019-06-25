import sys

from behave import *

sys.path.append("../../..")

from src.group_recommender import *


@given("a user with id {user_id:d}")
def step_impl(context, user_id):
    """
    :param user_id: id of a user
    :type context: behave.runner.Context
    """
    context.user = user_id


@when("the user wants recommended recipes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.recommendations = aggregated_voting([context.user])


@then("The recommendation system returns a list of recipes that matches the user's history and preferences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.recommendations != []


@given("a group of users with ids: {user1_id:d}, {user2_id:d}, {user3_id:d}")
def step_impl(context, user1_id, user2_id, user3_id):
    context.user1 = user1_id
    context.user2 = user2_id
    context.user3 = user3_id
    context.groupe = [context.user1, context.user2, context.user3]


@when("the host wants recommended recipes for its group")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.group_recommendation = aggregated_voting(context.groupe)
    context.fridge = ast.literal_eval(get_group_profils(context.groupe))[2]


@then("the recommendation system returns a list of recipes that matches all user's history and preferences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.group_recommendation != []
