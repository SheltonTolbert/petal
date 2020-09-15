import MediumGetter
import RedditGetter
import TwitterGetter
import DatabaseConnector as dbc
import Sorter


def get_reddit_content(username):
    reddit_content = []
    reddit_group = dbc.get_content(username, 'reddit')

    for subreddits in reddit_group:
        limit = 5
        reddit_content += RedditGetter.get_info(subreddits, limit)

    reddit_content.sort(key=lambda post: post.time)

    return reddit_content


def get_medium_content(username):
    medium_content = []
    medium_categories = dbc.get_content(username, 'medium')

    for categories in medium_categories:
        medium_content += MediumGetter.get_articles(categories)

    medium_content.sort(reverse=True, key=lambda article: article.date)

    return medium_content


def get_twitter_content(username):
    twitter_content = []
    twitter_users = dbc.get_content(username, 'twitter')
    TwitterGetter.connect()

    for users in twitter_users:
        twitter_content += TwitterGetter.get_content(users)

    twitter_content.sort(key=lambda tweet: tweet.time_created)

    return twitter_content


def get_content(username):
    '''
    get content from MySqlServer
        username:
            reddit_content == a list of subreddits
            medium_content == a list of medium categories
            twitter_content == a list of twitter usernames
    '''

    return(get_twitter_content(username), get_reddit_content(username), get_medium_content(username))


def get_user_info(username):
    userinfo = {}

    userinfo['username'] = username
    userinfo['subreddits'] = dbc.get_content(username, 'reddit')
    userinfo['twitter_following'] = dbc.get_content(username, 'twitter')
    userinfo['medium_categories'] = dbc.get_content(username, 'medium')

    return userinfo


if __name__ == "__main__":
    get_content('admin')
