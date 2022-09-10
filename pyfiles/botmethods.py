import tweepy    
from random import randint
#get keys
#keys[0]=api,keys[1]=apisec,keys[2]=at,keys[3]=atsec keys[4]=beartoken

keys = []

#open file relative to main.py
f = open("./text_files/keys.txt")
for l in f:
    l.strip()
    temp = l.split()
    keys.append(temp[1])
f.close()

#connect to API with v1.1
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth=auth)

class Bot:
    def __init__(self):
        self.mediaIds = []

    def populateMedia(self):
        m = open("./text_files/medialist.txt")
        for l in m:
            self.mediaIds.append(l.strip())
        m.close()
        return 

    def makeTweet(self):
        self.populateMedia()
        media_ids=[]
        i = randint(0,(len(self.mediaIds))-1)
        media_ids.append(api.media_upload(self.mediaIds[i]).media_id)
        api.update_status(status="",media_ids=media_ids)
        return
