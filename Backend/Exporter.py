import Driver
import json

'''
the purpose of this .py is to export all necessary data to a json file

Tweet(self, username, profile_img, retweet_count, favorited_count, time_created, text, media):
		self.username = username
		self.profile_img = profile_img
		self.retweet_count = retweet_count
		self.favorited_count = favorited_count
		self.time_created = time_created
		self.text = text
		self.media = media

Article(self, title, description, author, link, date, read_time, category):
		self.title = title
		self.description = description
		self.author = author
		self.link = link
		self.date = date
		self.read_time = read_time
		self.category = category

Post(self, title, author, link, score, time):
		self.title = title
		self.author = author
		self.link = link
		self.time = time
		self.score = score
'''


def export(username):
    try:
        content = Driver.get_content(username)
        info = Driver.get_user_info(username)

        package = {}
        reddit = {}
        twitter = {}
        medium = {}

        package['reddit'] = reddit
        package['twitter'] = twitter
        package['medium'] = medium
        package['user_info'] = info
    # twitter group
        for i in range(len(content[0][0])):
            post = {}
            post['username'] = content[0][0][i].username
            post['profile_img'] = content[0][0][i].profile_img
            post['text'] = content[0][0][i].text
            post['media'] = content[0][0][i].media
            post['retweet count'] = content[0][0][i].retweet_count
            post['favorited count'] = content[0][0][i].favorited_count
            post['time created'] = content[0][0][i].time_created
            twitter['post' + str(i)] = post
        # reddit Group
        for i in range(len(content[1][0])):
            post = {}
            post['title'] = content[1][0][i].title
            post['author'] = content[1][0][i].author
            post['link'] = content[1][0][i].link
            post['time'] = content[1][0][i].time
            post['score'] = content[1][0][i].score
            reddit['post' + str(i)] = post
        # medium Group
        for i in range(len(content[1][0])):
            post = {}
            post['author'] = (content[2][0][i].author)
            post['title'] = (content[2][0][i].title)
            post['description'] = (content[2][0][i].description)
            post['link'] = (content[2][0][i].link)
            post['date'] = (content[2][0][i].date)
            post['read_time'] = (content[2][0][i].read_time)
            post['category'] = (content[2][0][i].category)
            medium['post' + str(i)] = post

            with open('data.json', 'w') as outfile:
                json.dump(package, outfile)

            return True

    except:
        print('Error in JSON export')
        return False


export('admin')
