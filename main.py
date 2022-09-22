from pyfiles.botmethods import Bot
from time import sleep

#1) USE THIS IF USING A CRONJOB TO DEPLOY:
bot = Bot()
bot.makeTweet()

#2 USE THIS IF USING A CRONJOB TO DEPLOY:
#bot = Bot()
#running = True
#while running:
#    bot.makeTweet()
#    ##wait N many seconds. 3600 seconds = 1 hour
#    sleep(3600)
