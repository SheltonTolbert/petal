import MediumGetter
import RedditGetter
import TwitterGetter
import DatabaseConnector as dbc


def get_content(username):
    '''
    get content from MySqlServer
        username:
            reddit_content = a list of subreddits
            medium_content = a list of medium categories
            twitter_content = a list of twitter usernames
    '''

    reddit_content = []
    reddit_group = dbc.get_content(username, 'reddit')

    for subreddits in reddit_group:

        limit = 5
        reddit_content.append(RedditGetter.get_info(subreddits, limit))

    medium_content = []
    medium_categories = dbc.get_content(username, 'medium')

    for categories in medium_categories:
        medium_content.append(MediumGetter.get_articles(categories))

    twitter_content = []
    twitter_users = dbc.get_content(username, 'twitter')

    for users in twitter_users:
        TwitterGetter.connect()
        twitter_content.append(TwitterGetter.get_content(users))

    return(twitter_content, reddit_content, medium_content)


def get_user_info(username):
    userinfo = {}

    userinfo['username'] = username
    userinfo['subreddits'] = dbc.get_content(username, 'reddit')
    userinfo['twitter_following'] = dbc.get_content(username, 'twitter')
    userinfo['medium_categories'] = dbc.get_content(username, 'medium')

    return userinfo


get_content('admin')
