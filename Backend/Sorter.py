from datetime import datetime


def twitter_helper(tweet):
    return tweet.time_created


def sort_twitter(tweets):
    # tweets[0].sort(key=twitter_helper)
    tweets[0].sort(key=lambda tweet: tweet.time_created)

    print(type(tweets[0][0]))
    for tweet in tweets[0]:

        print(tweet.time_created)


def sort_reddit(posts):
    pass


def sort_medium(articles):
    pass
