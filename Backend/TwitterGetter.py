import tweepy
import json

'''
API Key = aJKIZuFnNZ5iigLEtWV7eqTzW
API Secret Key = Zec2irsel9V4f8Mlr6IRvNhWCSBovMervBZ3HKO3PDWQHwaHcn
Bearer token = AAAAAAAAAAAAAAAAAAAAAPDBGgEAAAAAzw4GDIXRtNtHzCmC0fBeRXgLQ9Q%3DAo3UyjSUSevT42ddactTB7sKKy4lA4CFcLDmydOw0cqcCedA5U
Access Token = 1285776217191448582-H5nEtjOOLxWAOsYLx4hCjEkfzUeUrW
Access Token Secret = khkAjL17STsYKuMK37D3s70QjilR76GmLYSOaQJBO9XVY
'''
token = 'aJKIZuFnNZ5iigLEtWV7eqTzW'
token_secret = 'Zec2irsel9V4f8Mlr6IRvNhWCSBovMervBZ3HKO3PDWQHwaHcn'
consumer_key = '1285776217191448582-H5nEtjOOLxWAOsYLx4hCjEkfzUeUrW'
consumer_secret = 'khkAjL17STsYKuMK37D3s70QjilR76GmLYSOaQJBO9XVY'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPDBGgEAAAAAzw4GDIXRtNtHzCmC0fBeRXgLQ9Q%3DAo3UyjSUSevT42ddactTB7sKKy4lA4CFcLDmydOw0cqcCedA5U'
api = None


class Tweet():

    def __init__(self, username, profile_img, retweet_count, favorited_count, time_created, text, media):
        self.username = username
        self.profile_img = profile_img
        self.retweet_count = retweet_count
        self.favorited_count = favorited_count
        self.time_created = time_created
        self.text = text
        self.media = media


def connect():
    global api
    auth = tweepy.OAuthHandler(token, token_secret)
    auth.set_access_token(consumer_key, consumer_secret)
    api = tweepy.API(auth)


def get_image(username):
    return api.get_user(username).profile_image_url


def get_recent_tweets(username):
    tweets = []
    public_tweets = api.user_timeline(username)

    for tweet in public_tweets:
        tweets.append(tweet)

    return tweets


def get_content(username):

    tweets = get_recent_tweets(username)

    content = []

    for tweet in tweets:

        json_str = json.dumps(tweet._json)
        parsed = json.loads(json_str)

        # json data extraction
        username = (parsed.get('user').get('screen_name'))
        profile_img = (parsed.get('user').get('profile_image_url'))
        retweet_count = parsed.get('retweet_count')
        favorited_count = parsed.get('favorited_count')
        time_created = parsed.get('created_at')
        text = parsed.get('text')

        # attempt to retrieve image/video media
        try:
            media = parsed.get('extended_entities').get(
                'media').get('media_url_https')
        except:
            # no media is present in tweet
            media = None
            pass

        content.append(Tweet(username, profile_img, retweet_count,
                             favorited_count, time_created, text, media))

    return content


if __name__ == "__main__":

    connect()
    print(get_image('Twitter'))

    print(get_content('elonmusk'))
    pass

#print(json.dumps(parsed, indent=4, sort_keys=True))
