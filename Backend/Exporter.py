import Driver
import json
import shutil

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
        self.image = image

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
        postnum = 0

        for i in range(len(content[0])):
            post = {}
            post['username'] = content[0][i].username
            post['profile_img'] = content[0][i].profile_img
            post['text'] = content[0][i].text
            post['media'] = content[0][i].media
            post['retweet count'] = content[0][i].retweet_count
            post['favorited count'] = content[0][i].favorited_count
            post['time created'] = content[0][i].time_created
            twitter['post' + str(postnum)] = post
            postnum += 1

    # reddit Group
        postnum = 0

        for i in range(len(content[1])):
            post = {}
            post['title'] = content[1][i].title
            post['author'] = content[1][i].author
            post['link'] = content[1][i].link
            post['time'] = content[1][i].time
            post['score'] = content[1][i].score
            reddit['post' + str(postnum)] = post
            postnum += 1

    # medium Group
        postnum = 0

        for i in range(len(content[2])):
            post = {}
            post['author'] = (content[2][i].author)
            post['title'] = (content[2][i].title)
            post['description'] = (content[2][i].description)
            post['link'] = (content[2][i].link)
            post['date'] = (content[2][i].date)
            post['read_time'] = (content[2][i].read_time)
            post['category'] = (content[2][i].category)
            post['image'] = (content[2][i].image)
            medium['post' + str(postnum)] = post
            postnum += 1

        with open('data.json', 'w') as outfile:
            json.dump(package, outfile)

        return True

    except:
        print('Error in JSON export')
        return False

# exports json as js file -- depracated


def js_export():
    json = open('data.txt', 'r')
    jsontxt = json.readlines()
    jsontxt = 'default export const Jsonpackage = {' + str(jsontxt)[
        3::][:-3] + '}'
    json.close()

    js = open('Jsonpackage.js', 'w')
    js.write(jsontxt)
    js.close()


def move():
    shutil.copy('data.json', '../petal/src')


if __name__ == "__main__":
    export('admin')
    move()
