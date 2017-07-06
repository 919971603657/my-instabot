import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer



APP_ACCESS_TOKEN = '3266493061.0fc22e0.6a076df329a64a97b3e091f99310eccb'
#Token Owner : vivekkumarsingh.main
#Sandbox Users : princechauhan3133,abhishekkumar11

BASE_URL = 'https://api.instagram.com/v1/'


#Function declaration to get your own info



def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'



#Function declaration to get the ID of a user by username



def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()





#Function declaration to get the info of a user by username



def get_user_info(insta_username):
    user_id = get_user_id()
    if user_id == 1:
        print 'User  exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is  data for this user!'
    else:
        print 'Status code other than 200 received!'



    #Function declaration to get your recent post



def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print ' image has been downloaded!'
        else:
            print 'Post  exist!'
    else:
        print 'Status code other than 200 received!'



#Function declaration to get the recent post of a user by username



def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id ==1:
        print 'User  exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print ' image has been downloaded!'
        else:
            print 'Post  exist!'
    else:
        print 'Status code other than 200 received!'



#Function declaration to like the recent post of a user



def like_a_post(insta_username):
    media_id = get_user_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

#function declaration to show list of like to the recent post of a user

#def liked_by_user(insta_username):
 #   media_id = get_user_id(insta_username)
  #  print "Get request URL:" + ((BASE_URL + "users/self/media/liked?access_token=%s")  % (APP_ACCESS_TOKEN))
   # liked = requests.get((BASE_URL + "users/self/media/liked?access_token=%s")  % (media_id, APP_ACCESS_TOKEN))
    #print liked["data"][0]["id"]






def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to my instaBot!'
        print 'Here are the menu options:'
        print "a.Get  own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get  own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Like the recent post of a user\n"
     #   print "f.Get a list of people who have liked the recent post of a user\n"
        print "j.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "e":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
      #  elif choice == "f":
       #     insta_username = raw_input("Enter the username of the user: ")
        #    liked_by_user(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()

