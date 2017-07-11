import requests
import urllib
import json
import termcolor
import time
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from clarifai.rest import ClarifaiApp

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer



APP_ACCESS_TOKEN = '3266493061.0fc22e0.6a076df329a64a97b3e091f99310eccb'
#Token Owner : vivekkumarsingh.main
#list_of_sandbox  : ['princechauhan3133','abhishekkumar11','cmayankdogra', 'gaur_abhishek']

BASE_URL = 'https://api.instagram.com/v1/'
ar = [] #define array
my_dict = {
    'imageurl': None, #defining dictionary and stored imageurl and words
    'words': ''

}
user_lis = ['princechauhan3133', 'cmayankdogra']



#Function declaration to get your own info


#fetching details of yourself:
def fetch_self_info():
    #define request url
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    #print get reques url
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#check if request status ok
    if user_info['meta']['code'] == 200:
        #check if user media has data
        if len(user_info['data']):
            print termcolor.colored('Username: %s' % (user_info['data']['username']),'red')
            print termcolor.colored('No. of followers: %s' % (user_info['data']['counts']['followed_by']),'red')
            print termcolor.colored('No. of people you are following: %s' % (user_info['data']['counts']['follows']),'red')
            print termcolor.colored('No. of posts: %s' % (user_info['data']['counts']['media']),'red')

        else:
            #display appropriate message
            print 'User data not exist!'
    else:
            print termcolor.colored('Status code other than 200 received','blue')









#Function declaration to get the ID of a user by username

#fetching username from user id

def get_user_id(insta_username):
    #define request url
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    #print get request url
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#check if request status ok
    if  user_info['meta']['code'] == 200:
        #check if user media has data
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print termcolor.colored('Status code other than 200 received!','red')
        exit()





#Function declaration to get the info of a user by username


#fetching user information
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User not exist'
        exit()
        #define request url
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    #print get request url
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#check if the status request ok
    if user_info['meta']['code'] == 200:
        #check if user media has data
        if len(user_info['data']):
            #print username which has own information
            print termcolor.colored('Username: %s' % (user_info['data']['username']),'blue')
            #print user no of followers
            print termcolor.colored('No. of followers: %s' % (user_info['data']['counts']['followed_by']),'blue')


#print user no of posts
            print termcolor.colored('No. of posts: %s' % (user_info['data']['counts']['media']),'blue')
        else:
            print termcolor.colored(' no data for this user!','blue')
    else:
        print termcolor.colored('Status code other than 200 received!','blue')



    #Function declaration to get your recent post


#fetching post of user
def get_own_post():
    #define request url
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    #print get request
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
#check if the status request is ok
    if own_media['meta']['code'] == 200:
        #check if user media has data
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            #checking the image url is been in standard resolution
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            #retrieving the image url,image name
            urllib.urlretrieve(image_url, image_name)
            #print the image has been downloaded and is in standard resolution
            print termcolor.colored(' image has been  downloaded!','red')
        else:
           print termcolor.colored('Post does not exist!','red')
    else:
        print termcolor.colored( 'Status code other than 200 received!','red')

#Function declaration to get the recent post of a user by username


#fetching details of user post
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User not exist!'
        exit()
        #define request url
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    #print get request url
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
#checking status request is ok
    if user_media['meta']['code'] == 200:
        #checking if user media has data
        if len(user_media['data']):
            #show the condition to download image
            ch = raw_input("Do you want to download image  (y/n):")
            # if condition show  yes then downloaded
            if ch.upper() == 'Y':
                #image show in jpeg format
             image_name = user_media['data'][0]['id'] + '.jpeg'
                #image show in low resolution
            image_url = user_media['data'][0]['images']['low_resolution']['url']
            #retrieve the image url and image name
            urllib.urlretrieve(image_url, image_name)
            #print image has been downloaded
            print termcolor.colored(' image has been downloaded!','blue')
        else:
            print termcolor.colored('Post not  exist!','blue')
    else:
        print termcolor.colored('Status code other than 200 received!','blue')



#Function declaration to like the recent post of a user


#fetching the user recent post that like
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    #define request url
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    #print requesr url that have been posted by user
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    #check the status request is ok
    if post_a_like['meta']['code'] == 200:
        #print liked the pic that have been posted by user
        print termcolor.colored(' You have Liked the pic successfully! ','red')
    else:
        print termcolor.colored(' status  code other than 200 received!','red')

#fetching user recent post unlike
def unlike_a_post(insta_username):
    media_id = get_post_id(insta_username)
    #define request url
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_unlike = requests.delete(request_url).json()
    #check the status request is ok
    if post_a_unlike['meta']['code'] == 200:
        #print unlik the post post by user
        print ' You have unLiked the pic successfully! '
    else:
        print ' status  code other than 200 received!'



#fetching post id of a user
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "User not exist!"
        exit()
        #define request url
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id , APP_ACCESS_TOKEN)
    #print get request url
    print  "GET request url : %s"  % (request_url)
    user_media = requests.get(request_url).json()
    print user_media
#check status request is 200
    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            #print no recent post of a user
            print termcolor.colored("no recent post of the user",'red')
            exit()
    else:
        print termcolor.colored("Invalid request",'red')
        exit()

#function declaration to show list of like to the recent post of a user
#fetching list of like by user on a recent post
def get_list_like(insta_username):
    media_id = get_post_id(insta_username)
#define request url
    request_url=(BASE_URL + "media/%s/likes/?access_token=%s") % (media_id,APP_ACCESS_TOKEN)
    #print get request
    print "Get request url : %s" % (request_url)
    list = requests.get(request_url).json()
    #check status request is 200
    if list["meta"]["code"] == 200:
        #print list of user
        print termcolor.colored( 'list','red')
    else:
        print termcolor.colored( "Unsuccessful",'red')

#function declaration to show post comment to the recent post of the user
#fetching comment posted by a user
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    #define request url
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()
#check status code is ok
    if make_comment['meta']['code'] == 200:
        #print  added new comment
        print termcolor.colored("Successfully added a new comment!",'red')
    else:
        print termcolor.colored( "Unable to add comment. Try again!",'red')

#function declaration to show list of comment to the recent post of the user
#fetching list of comment by a user
def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    #define request url
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id , APP_ACCESS_TOKEN)
    comment_list = requests.get(request_url).json()
    #check status request is ok
    if comment_list['meta']['code'] == 200:
       if len(comment_list['data']):
           for i in range(0, len(comment_list['data'])):
               print comment_list['data'][i]['text']
       else:
           #print no recent post of user
          print termcolor.colored( 'No recent post of the user','red')
          exit()
    else:
       print termcolor.colored('status code other than 200 received','red')
       exit()


#fetching deleting negative comment by a user
def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    #define request url
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    #print get request
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
#check status request is ok
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()
                    #checking status request is ok
                    if delete_info['meta']['code'] == 200:
                        #print deleted comment successfully
                        print termcolor.colored( 'Comment successfully deleted!\n','red')
                    else:
                        print termcolor.colored('Unable to delete comment!','red')
                else:
                    print termcolor.colored('Positive comment : %s\n','red)' % (comment_text))
        else:
            print termcolor.colored(' No existing comments on the post!','red')
    else:
        print termcolor.colored ('Status code other than 200 received!','red')




 #function to show the subtrend of a fooditems and plot through wordcloud

#objective to show subtrend of any activities or event and plot through word cloud
#defining clarifaiApp and generate key
app = ClarifaiApp(api_key='df3f6b49a55048579101375b3ac757bf')

# get the general model
model = app.models.get('food-items-v1.0')
for user in user_lis:
    def get_users_post(user):
        user_id = get_user_id(user)
        if user_id == None:
            print 'User does not exist!'
            exit()
        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_media = requests.get(request_url).json()

        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                model = app.models.get('food-items-v1.0')
                response = model.predict_by_url(url=image_url)
                #data fetched through concepts and stored in response
                for x in response['outputs'][0]['data']['concepts']:
                    #print name stored in value
                    print x['name'], x['value']
                    #if value of x greater than .7
                    if x['value'] > .7:
                        #string show the value of x in name
                        strr = x['name']
                        #using temp variable to fetch words stored in dictionary
                        temp = my_dict['words']
                        temp = temp + ' ' + str(strr)
                        my_dict['words'] = temp
                        #string stored in a dictionary as a words
                String = my_dict['words']
                print
                wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=1200, height=1000).generate(
                    String)
                plt.imshow(wordcloud)
                plt.axis('off')
                plt.show()
                urllib.urlretrieve(image_url, image_name)
            else:
                print "error"

        else:
            print "error"


def start_bot():
    global ch
    while True:
        time.sleep(2)
        print termcolor.colored('Hey! Welcome to my instaBot!','blue')
        print termcolor.colored('Here are the menu options:','blue')
        print termcolor.colored("a.Get  own details\n",'red')
        print termcolor.colored("b.Get details of a user by username\n",'red')
        print termcolor.colored("c.Get  own recent post\n",'red')
        print termcolor.colored("d.Get the recent post of a user by username\n",'red')
        print termcolor.colored("e.Like the recent post of a user\n",'red')
        print termcolor.colored ("f.Get a list of people who have liked the recent post of a user\n",'red')
        print termcolor.colored("g.Make a comment on the recent post of a user\n",'red')
        print termcolor.colored("h.List of comment on the recent post of a user\n" ,'red')
        print termcolor.colored("i.Delete negative comments from the recent post of a user\n", 'red')
        print termcolor.colored ("j.Unlike most recent post of a user\n",'red')
        print termcolor.colored("k.SHOW SUBTREND OF FOOD EATEN \n",'red')
        print termcolor.colored("l.Exit",'red')

        choice = raw_input("Enter you choice: ")
        if choice == "a":

          fetch_self_info()
          time.sleep(2)
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
            time.sleep(2)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
            time.sleep(2)
        elif choice == "e":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
            time.sleep(2)
        elif choice == "f":
            insta_username = raw_input("Enter the username of the user: ")
            get_list_like(insta_username)
            time.sleep(2)
        elif choice == "g":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
            time.sleep(2)
        elif choice == "h":
            insta_username = raw_input("Enter the username of the user: ")
            get_comment_list(insta_username)
            time.sleep(2)
        elif choice == "i":
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
            time.sleep(2)
        elif choice == "j":
            insta_username = raw_input("Enter the username of the user:")
            unlike_a_post(insta_username)
            time.sleep(2)
        elif choice == "k":
            get_users_post(user)
        elif choice == "l":
            exit()
        else:
          print "Invalid choice"


start_bot()

