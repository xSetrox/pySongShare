# pySongShare
Automatically send tweets on what songs you like on Spotify!

# Requirements
Simply run `pip install -r requirements.txt` to satisfy all requirements. Or install manually with `pip install package`:
```
tweepy==3.8.0
spotipy==2.4.4
```
# Setup
The variables for setup are defined in source code! Which is ugly. I'll add a better way to store these I promise.
You will need API keys for Spotify and Twitter, therefore you will need to create a developer profile on both.
### Twitter
Go to https://developer.twitter.com , do their very tedious setup, and make an app. What you need will be in the keys and 
tokens tab of your app. 
You must click create the "access token and access token secret" parts.
Fill lines `12-15` with Twitter API keys. 

```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```
### Spotify
Go to https://developer.spotify.com , sign up, and create an app. Get the client id and secret and fill them in in
lines 19 and 20:
```
os.environ["SPOTIPY_CLIENT_ID"] = ''
os.environ["SPOTIPY_CLIENT_SECRET"] = ''
```
Now the important part: The redirect URL. This is very important, but it can be literally anything. Doesn't need to be a working
webpage.
You don't need to edit the code for this part unless you'd like to change it from http://localhost:8888.
Edit settings on your app (or if you're still making it, scroll down to redirect url) and set this to match whatever URL you
filled in in line 23 of your code:
```
# make sure the redirect url here matches the one you set on the Spotify dev website. it doesnt matter what you choose.
# it can be a website you dont own or lead to a non-existent one.
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8888'`
```

## The token
You're pretty much done, but the first time you run the app it will open a web page asking if you'd like to grant access.
Click accept of course. Once you do this it will open your redirect URL; it will add a lot of characters after it. These
are important. Copy and paste the entire redirect URL and go back to the python commandline. You will see it asking for
the redirect URL. Paste it in and you should be good. 

# Usage
As long as you properly set this up it should work automatically. Go and like a song on Spotify while running it and it will
print info as well as tweet it. 

# Why the prevlikes.txt?
tl;dr: The .txt stores ID's of the songs you've liked to prevent them from being tweeted again.

The API function I used returns an entire playlist of liked songs. I passed an argument to it to return the last
liked song, but this method (seemingly the only with this API) will screw up if you unlike the last liked song, because
the "last liked song" will then be different. So when a song like is detected, this will check the list of song ID's to
make sure it isn't repeating a tweet, and if it's not on the list, it will tweet it and then add it to the list so it's never
tweeted again. 
