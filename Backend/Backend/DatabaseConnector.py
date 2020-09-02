import mysql.connector

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


def __get_id(username):
    try:
        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        query = ("SELECT id FROM users WHERE username = '%s';")
        cursor.execute(query % username)

        for items in cursor:
            userid = int(str(items)[1::][:-2])

        cursor.close()
        conn.close()

        return userid
    except:
        print('ERROR: username does not exist')
        return None


def get_content(username, platform):
    try:
        content = []

        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        userid = __get_id(username)

        query = "SELECT content from user_content where platform = '%s' AND id = %s;"
        data = (platform, userid)

        cursor.execute(query % data)

        for items in cursor:
            content.append(items[0])

        cursor.close()
        conn.close()

        return content
    except:
        return False


def insert(username, platform, content):

    try:
        userid = __get_id(username)

        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        # check to see if duplicate entry
        for i in get_content(username, platform):
            if content in i:
                return False

        query = "INSERT IGNORE INTO user_content (id, platform, content) VALUES ( %s, '%s', '%s');"
        data = (userid, platform, content)

        cursor.execute(query % data)
        conn.commit()

        cursor.close()
        conn.close()
        return True

    except:
        return False


def remove(username, platform, content):
    try:
        userid = __get_id(username)

        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        query = "DELETE FROM user_content Where id = %s AND platform = '%s' AND content = '%s';"
        data = (userid, platform, content)

        cursor.execute(query % data)
        conn.commit()

        cursor.close()
        conn.close()
        return True

    except:
        return False


def create_user(username, email):
    if __get_id(username) != None:
        print('ERROR: username not available')
        return False
    else:
        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        query = "INSERT INTO users (username, email) VALUES('%s', '%s');"
        data = (username, email)

        cursor.execute(query % data)
        conn.commit()

        cursor.close()
        conn.close()
        return True


def delete_user(username):
    if __get_id(username) == None:
        print('ERROR: no such username')
        return False
    else:
        conn = mysql.connector.Connect(
            host="localhost", user="root", password="password", database="petal")
        cursor = conn.cursor(buffered=True)

        userid = __get_id(username)

        query = "DELETE from users where id = %s;"

        cursor.execute(query % userid)
        conn.commit()

        cursor.close()
        conn.close()
        return True
