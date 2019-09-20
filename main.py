import spotipy
import os
import spotipy.util as util
import time
import tweepy

# enter your name here to customize. your "username" MUST be your spotify username!
yourname = "John"
username = "john.cena"

# ************ Twitter API keys go here ************
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# ************************************************

# ************ enter your spotify api keys here ************
os.environ["SPOTIPY_CLIENT_ID"] = ''
os.environ["SPOTIPY_CLIENT_SECRET"] = ''
# make sure the redirect url here matches the one you set on the Spotify dev website. it doesnt matter what you choose.
# it can be a website you dont own or lead to a non-existent one.
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8888'
# ************************************************

# leave everything below this line alone
# ***************************************************************************************************************
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)
oldvar = ""
def isinfile(file, query):
    if query in file:
        return True
    return False


if token:
    sp = spotipy.Spotify(auth=token)
    print("Token accepted, running")
    while True:
        results = sp.current_user_saved_tracks(1, 0)
        item = results['items'][0]['track']
        if item != oldvar:
            trackname = item['name']
            artists = item['artists'][0]['name']
            # does the previous likes thing have this on record already?
            prevfile = open("prevlikes.txt", "r+")
            if not isinfile(prevfile, item['id']):
                prevfile.write("\n" + item['id'])
                print(
                    yourname + " just liked " + trackname + " by " + artists + " on Spotify:\n" + item['external_urls']['spotify'])
                twitter.update_status(
                    yourname + " just liked " + trackname + " by " + artists + " on Spotify:\n" + item['external_urls']['spotify'])
            oldvar = item
            prevfile.close()
        time.sleep(10)

else:
    print("Can't get token for", username)
