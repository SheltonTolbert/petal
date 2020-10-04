## petal
Petal is a social media data aggregation project which leverages external API's, such as Twitter and reddit, and good-old-fassioned webscraping to retrieve data from the web.
\n
\n




#### front-end
The UI was made using React, traditional html and css






#### backend




## app.yp
  Flask app -- Refer to API






## DatabaseConnector.py
  An Python interface for MySQL
  '''
  __get_id(): 
    -private method for retreving user id
    -returns None if no such username

  get_content(username, platform):
      -returns all content associated with username 
      -returns False if no such username

  insert(username, platform, content):
      -inserts new content categories 
      -returns false error, true if successful

  remove(username, platform, content):
      -removes category from platform
      -returns true if successful else false

  create_user(username, email):
      -creates new user 
      -throws error if user is duplicate entry
      -else returns true

  delete_user(username): 
      -deletes user
      -throws error if username does not exist
      -else returns true
  '''
## Driver.py
Driver code for retrieving and formatting lage batch data
  '''
  //TODO: add post limit variable
  get_reddit_content(username):
    retrieves data from every subreddit in the user object
    returns list
  
  get_medium_content(username):
    retrieves data from every category in the user object
    returns list
    
  //TODO: add post limit variable    
  get_twitter_content(username):
    retrieves data from every subreddit in the user object
    returns list
    
  get content from MySqlServer
    username:
      reddit_content == a list of subreddits
      medium_content == a list of medium categories
      twitter_content == a list of twitter usernames
    returns (twitter_content[], reddit_content[], medium_content[])
    
    '''
  


## Exporter.py

the purpose of this .py is to export all necessary data to a json file
'''
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



## MediumGetter.py
 '''
  class Article():
    def __init__(self, title, description, author, link, date, read_time, category, image):
        self.title = title
        self.description = description
        self.author = author
        self.link = link
        self.date = date
        self.read_time = read_time
        self.category = category
        self.image = image
  
  get_articles(category):
    returns Article 
  
  
  '''
  
  
  
## RedditGetter.py
'''
  class Post():

    def __init__(self, title, author, link, score, time):
        self.title = title
        self.author = author
        self.link = link
        self.time = time
        self.score = score
        
    get_title(sub, limit):
      returns string[] titles
      
    def get_url(sub, limit):
      returns string[] urls   
      
    def get_author(sub, limit):
      returns string[] author_names
   
    def get_score(sub, limit):
      returns string[] post_scores
      
    def get_time(sub, limit):
      returns string[] post_times      
      
    def get_info(sub, limit):
      returns Post[]posts
  
  
  '''
      
 

## Sorter.py
'''
  --depricated
  
  
  '''
  
  
## TwitterGetter.py
'''
  class Tweet():

    def __init__(self, username, profile_img, retweet_count, favorited_count, time_created, text, media):
        self.username = username
        self.profile_img = profile_img
        self.retweet_count = retweet_count
        self.favorited_count = favorited_count
        self.time_created = time_created
        self.text = text
        self.media = media
   
  get_image(username):
    returns image url for given username
  
  def get_recent_tweets(username):
      returns a json object containing information of each recent tweet of the username - up to 11
    
  def get_content(username):
      returns a Tweet object for each recent tweet of the username - up to 11
 '''     
  
  
## API   
