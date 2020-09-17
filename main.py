import spotipy
import os
import spotipy.util as util
import time
import tweepy
import configparser

# ----------
# you shouldnt be touching this file unless you're purposefully changing how pysongshare works
# everything config-related goes into config.ini
# ----------

cparser = configparser.ConfigParser()
cparser.read('config.ini')
yourname = cparser['config']['yourname']
username = cparser['config']['username']
consumer_key = cparser['config']['consumer_key']
consumer_secret = cparser['config']['consumer_secret']
access_token = cparser['config']['access_token']
access_token_secret = cparser['config']['access_token_secret']
os.environ["SPOTIPY_CLIENT_ID"] = cparser['config']['spotipy_client_id']
os.environ["SPOTIPY_CLIENT_SECRET"] = cparser['config']['spotipy_client_secret']
os.environ["SPOTIPY_REDIRECT_URI"] = cparser['config']['spotipy_redirect_uri']

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
                print(f'{yourname} just liked {trackname} by {artists} on Spotify:\n' + item['external_urls']['spotify'])
                twitter.update_status(f'{yourname} just liked {trackname} by {artists} on Spotify:\n' + item['external_urls']['spotify'])
            oldvar = item
            prevfile.close()
        time.sleep(10)

else:
    print("Can't get token for", username)
    exit()
