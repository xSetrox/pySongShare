# pySongShare
<a href="url"><img src="https://i.imgur.com/T1ckd4x.png" align="center" height="200" width="200" ></a>
Automatically send tweets on what songs you like on Spotify! Runs on Python 3.


# Requirements
Simply run `pip install -r requirements.txt` to satisfy all requirements. Or install manually with `pip install package`:
```
tweepy==3.8.0
spotipy==2.4.4
```
# Setup
To set up, you need to fill out the config.ini. As you follow this guide, fill it out.
You will need API keys for Spotify and Twitter, therefore you will need to create a developer profile on both.
### Twitter
Go to https://developer.twitter.com , do their very tedious setup, and make an app. What you need will be in the keys and 
tokens tab of your app. 
You must click create the "access token and access token secret" parts.
Now fill out these parts of the config.ini with the info you see.

```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

### Spotify
Go to https://developer.spotify.com , sign up, and create an app. Get the client id and secret.
Now fill out these parts of the config.ini with the info you see.

```
SPOTIPY_CLIENT_ID = 
SPOTIPY_CLIENT_SECRET = 
```

Now the important part: The redirect URL. This is very important, but it can be literally anything. Doesn't need to be a working
webpage.
You don't need to edit the code for this part unless you'd like to change it from http://localhost:8888.
Edit settings on your app (or if you're still making it, scroll down to redirect url) and set this to match whatever URL you
filled in in the config.ini:

```
SPOTIPY_REDIRECT_URI = 'http://localhost:8888'
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
