import configparser
import requests
from random import randint, choice


config = configparser.ConfigParser()
config.read('bot.ini')

NUMBER_OF_USERS = int(config.get('MAIN_SETTINGS', 'number_of_users'))
MAX_POSTS_PER_USER = int(config.get('MAIN_SETTINGS', 'max_posts_per_user'))
MAX_LIKES_PER_USER = int(config.get('MAIN_SETTINGS', 'max_likes_per_user'))

BASE_URL = config.get('OTHER', 'base_url')

jwt_access_dict = {}


def sign_up():
    print('\n', 'SIGNING UP...')
    for i in range(NUMBER_OF_USERS):
        url = BASE_URL + 'api/signup/'
        email = "test" + str(i) + "@localhost"
        json = {"email":email, "password":"Pwd123@"}
        try:
            response = requests.post(url, json=json)
            print(response.status_code, response.json())
        except Exception as ex:
            print('ERROR:', 'User#:', i, email, 'Status code:', response.status_code, 'Exception:', ex)

def sign_in():
    print('\n', 'SIGNING IN...')
    for i in range(NUMBER_OF_USERS):
        url = BASE_URL + 'api/token/'
        email = "test" + str(i) + "@localhost"
        json = {"email":email, "password":"Pwd123@"}
        try:
            response = requests.post(url, json=json)
            jwt_access_dict[email] = ''
            jwt_access_dict[email] = response.json()['access']
            print('User#:', i, email, 'Status code:', response.status_code, 'JWT:', jwt_access_dict[email])
        except Exception as ex:
            print('ERROR:', 'User#:', i, email, 'Status code:', response.status_code, 'Exception:', ex)

def create_random_posts():
    print('\n', 'ADDING POSTS...')
    for i in range(NUMBER_OF_USERS):
        posts_per_user = randint(1, MAX_POSTS_PER_USER)
        email = "test" + str(i) + "@localhost"
        print(posts_per_user, 'post(s) per user', email)
        for post in range(posts_per_user):
            url = BASE_URL + 'api/posts/'
            json = {"title":"Post" + str(post) + " - " + email, "body":"body"}
            try:
                headers = {'Authorization': 'Bearer ' + jwt_access_dict[email]}
                response = requests.post(url, headers=headers, json=json)
                print('Post#', post, 'User#:', i, email, 'Status code:', response.status_code, response.json())
            except Exception as ex:
                print('ERROR:', 'Post#', post, 'User#:', i, email, 'Status code:', response.status_code, 'Exception:', ex)

def like_random_posts():
    print('\n', 'LIKING POSTS...')
    
    #Get a list of all post IDs
    url = BASE_URL + 'api/posts/'
    headers = {'Authorization': 'Bearer ' + jwt_access_dict["test0@localhost"]}
    response = requests.get(url, headers=headers)
    ids = [element['id'] for element in response.json()]
    
    for i in range(NUMBER_OF_USERS):
        likes_per_user = randint(1, MAX_LIKES_PER_USER)
        email = "test" + str(i) + "@localhost"
        print(likes_per_user, 'like(s) per user', email)
        for post in range(likes_per_user):
            #Select a random post to like
            post_to_like = str(choice(ids))

            url = BASE_URL + 'api/post_like/'
            json = {"post": post_to_like}
            try:
                headers = {'Authorization': 'Bearer ' + jwt_access_dict[email]}
                response = requests.post(url, headers=headers, json=json)
                print('Liking Post#', post, 'User#:', i, email, 'Status code:', response.status_code, response.json())
            except Exception as ex:
                print('ERROR:', 'Liking Post#', post, 'User#:', i, email, 'Status code:', response.status_code, 'Exception:', ex)


sign_up()
sign_in()
create_random_posts()
like_random_posts()
