import tweepy    
from random import randint
#get keys
#keys[0]=api,keys[1]=apisec,keys[2]=at,keys[3]=atsec keys[4]=beartoken

keys = []

#open file relative to main.py
file = open("./text-files/keys.txt")
for line in file:
    line.strip()
    temp = line.split()
    keys.append(temp[1])
file.close()

#connect to API with v1.1
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth=auth)

class Bot:
    def __init__(self):
        self.mMediaIds = []
    """
    Reads the medalist.txt file and adds file name to object list field
    """
    def populateMedia(self):
        mediaList = open("./text-files/medialist.txt")
        for line in mediaList:
            self.mMediaIds.append(line.strip())
        mediaList.close()

    """
    Picks a random media file to tweet out. Media file is sourced from media list field
    that reads from the medalist.txt file
    """
    def makeTweet(self):
        if(len(self.mMediaIds)<1):
            print("No media to tweet out")
            return
        media_ids=[]
        media_index = randint(0,(len(self.mMediaIds))-1)
        media_ids.append(api.media_upload(self.mMediaIds[media_index]).media_id)
        api.update_status(status="",media_ids=media_ids)

    """
    Likes any mentions
    """
    def likeMentions(self):
        for tweet in api.mentions_timeline():
            if not tweet.favorited:
                api.create_favorite(tweet.id)
        for tweet in api.get_retweets_of_me():
            if not tweet.favorited:
                api.create_favorite(tweet.id)
