from pyfiles.botmethods import Bot
from time import sleep

# MAKE SURE TO POPULATE MEDIA BEFORE TWEETING
#1) USE THIS IF USING A CRONJOB TO DEPLOY:
bot = Bot()
bot.populateMedia()
bot.makeTweet()

#2 USE THIS IF USING A INFINTE LOOP TO DEPLOY:
#bot = Bot()
#bot.populateMedia()
#running = True
#while running:
#    bot.makeTweet()
#    ##wait N many seconds. 3600 seconds = 1 hour
#    sleep(3600)
