"""
User-Based collaborative filtering recommendation system;
Collaborative Filtering is a method of making automatic predictions (filtering) about
the interests of a user by collecting preferences or taste information from many users (collaborating).
The underlying assumption of the collaborative filtering approach is that if a person A
has the same opinion as a person B on an issue, A is more likely to have B's opinion on a different
issue than that of a randomly chosen person.

This script requires that 'Pandas' and 'Surprise' be installed within the Python environment you are running
 this script in.

This file can also be imported as a module and contains the following
functions:
    * split_data_train_test - split the dataset "ratings" into two subset : trainset and testset
    * train - train the model to learn from the data using a prediction algorithm
    * predict - predict scores of users of items from learning the pattern learned in training the model
    * get_top_n - get the top n items for all user after training the model and predicting all scores of all items
    * store_top_recommendation - store the n top recommendations for all users in a separate csv file
"""
from collections import defaultdict

import pandas as pd
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split

# a dictionnary of recommendations of all users
recommendations = {}
bsl_options = {'method': 'als',
               'n_epochs': 5,
               'reg_u': 12,
               'reg_i': 5
               }
# a ratio to split the dataset into train/test sets
test_ratio = 0.15
# the items in our system (recipes) are rated from 0 to 5
rate_scale = (0, 5)


def open_csv(file):
    """
    a function that helps to open the cvs file of ratings of recipes by users
    :param file: a csv file
    :return: pandas dataframe containing scores of recipes given by users
    """
    print("Opening the csv file ....")
    df = pd.read_csv(file, sep=',', error_bad_lines=False, encoding="latin-1")
    df.columns = ['RecipeID', 'profileID', 'Rate']
    return df


def df_to_dataset(df):
    """
    Convert the dataframe retrieved from csv file to Dataset for Surprise module
    :param df: the Pandas dataframe of ratings
    :return: Surprise Dataset of ratings between 0 and 5
    """
    print("Converting to data set ....")
    reader = Reader(rating_scale=rate_scale)
    data = Dataset.load_from_df(df[['profileID', 'RecipeID', 'Rate']], reader)
    return data


def split_data_train_test(data, ratio=test_ratio):
    """
    Split the dataset into train/test sets for the model to learn the pattern of rating distribution
    :param data: Suprise Dataset
    :param ratio: The proportion of training set and test set for the model
    :return: a tuple of trainset and testset
    """
    print("Splitting the data into training and testing sets ....")
    trainset, testset = train_test_split(data, test_size=ratio)
    return trainset, testset


def train(trainset, testset):
    """
    Train the recommender model that uses the baseline algorithm which is based on similarities between users
    and their shared ratings of recipes
    :param trainset: the train set from which the model learns the pattern of ratings and similarity between different users
    :param testset: the testset to which the model validate its knowledge of data and ratings distribution
    :return: a variable containing predictions of ratings of all items given by all users
    """
    print("Training the model for prediction ....")
    # BaselineOnly algorithm gave us the best rmse,
    # therefore, we will train and predict with BaselineOnly and use Alternating Least Squares (ALS).
    algo = BaselineOnly(bsl_options=bsl_options)
    predictions = algo.fit(trainset).test(testset)
    return predictions


def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the tests method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''
    print("Getting the top " + str(n) + " recommendations for all users .....")
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def predict(trainset):
    print("Training the model for prediction .....")
    # predict ratings for all pairs (u, i) that are NOT in the training set.
    algo = BaselineOnly(bsl_options=bsl_options)
    testset = trainset.build_anti_testset()
    predictions = algo.fit(trainset).test(testset)
    return predictions


def build_recommendations(predictions, n=10):
    """
    Create a variable (dictionnary) that contains a number of top items recommended for each user
    :param predictions: The list of predictions, as returned by the tests method of an algorithm.
    :param n: The number of recommendation to output for each user. Default
            is 10.
    :return: A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """
    print("Creating the dictionary of suggestions for all users ....")
    top_n = get_top_n(predictions, n=n)
    # store the recommended items for each user
    for uid, user_ratings in top_n.items():
        # recommendations[uid] = [iid for (iid, _) in user_ratings]
        recommendations[uid] = [(iid, rating) for (iid, rating) in user_ratings]
        # print(uid, [iid for (iid, _) in user_ratings])
    return recommendations


def store_top_recommendation(recommendation):
    """
    store the dictionary output from building recommendations in a csv file to use later
    :param fridge: a list of ingredients
    :param recommendation: A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """
    df = pd.DataFrame(recommendation.items(), columns=['user_id', 'recommendations'])
    print("Storing recommendations in csv file....")
    df.to_csv(r'Res/recommendations.csv', index=None, header=True)


if __name__ == "__main__":
    # Read reviews table from csv file as dataframe for Pandas
    df = open_csv("Res/clean_reviews.csv")
    # Convert the data frame to be used with Surprise
    data = df_to_dataset(df)
    # Split the data into train set and tests set
    training, testing = split_data_train_test(data, test_ratio)
    # Predict ratings for pairs that are not in trainingSet
    predictions = predict(training)
    suggestions = build_recommendations(predictions, 20)
    store_top_recommendation(suggestions)
