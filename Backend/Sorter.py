from datetime import datetime


def twitter_helper(tweet):
    return tweet.time_created


def sort_twitter(tweets):
    return tweets[0].sort(key=lambda tweet: tweet.time_created)


def sort_reddit(posts):
    pass


def sort_medium(articles):
    pass
