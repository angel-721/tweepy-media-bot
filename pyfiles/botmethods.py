"""
This module wraps around tweepy and works with the database.

to make tweets and send media to Twitter

get keys
keys[0]=api,keys[1]=apisec,keys[2]=at,keys[3]=atsec keys[4]=beartoken
"""

import tweepy

from pyfiles.database import randomImage, randomKeyWordImage

keys = []

# open file relative to main.py
file = open('./text-files/keys.txt', encoding='utf-8')
for line in file:
    line.strip()
    temp = line.split()
    keys.append(temp[1])
file.close()

# connect to API with v1.1
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth=auth)


class Bot:
    """
    Picks random media file to tweet out. Media file is sourced from medialist.

    that reads from the medalist.txt file
    """

    def makeTweet(self):
        """Make a tweet."""

        image = randomImage()
        if image is None:
            print('No media to tweet out')
            return
        image = './media/' + image
        media_ids = []
        media_ids.append(api.media_upload(image).media_id)
        api.update_status(status='', media_ids=media_ids)
        return

    def makeKeyWordTweet(self, keyWord):
        """Works the same as makeTweet but uses a keyword."""

        image = randomKeyWordImage(keyWord)
        if image is None:
            print('No media to tweet out')
            return
        image = './media/' + image
        media_ids = []
        media_ids.append(api.media_upload(image).media_id)
        api.update_status(status='', media_ids=media_ids)
        return

    def likeMentions(self):
        """Likes any mentions."""

    for tweet in api.mentions_timeline():
        if not tweet.favorited:
            api.create_favorite(tweet.id)
