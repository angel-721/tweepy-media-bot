#!/usr/bin/python
import argparse
from time import sleep
from pyfiles.botmethods import Bot
from os import system

# MAKE SURE TO POPULATE MEDIA BEFORE TWEETING

# 1) USE THIS IF USING A CRONJOB TO DEPLOY:
def cronJobDeploy():
    bot = Bot()
    bot.populateMedia()
    bot.makeTweet()

# 2 USE THIS IF USING A INFINTE LOOP TO DEPLOY:
def loopDeploy():
    bot = Bot()
    bot.populateMedia()
    running = True
    while running:
        bot.makeTweet()
        # 3600 seconds = 1 hour
        sleep(3600)

"""
Function to parse cli arguments mainly for getting the type of deployment
"""
def parseArgs():
    parser = argparse.ArgumentParser(prog="Tweepy-Media-Bot", description="Tweets and Likes Media in a automated fasion")
    parser.add_argument("-deploy", type=str, required=True)
    args = parser.parse_args()
    return args

# testing to come soon!
def main(args):
    #   if (args.deploy == "test"):
    #       system("./test.py")
    if (args.deploy == "cronjob"):
        cronJobDeploy()
    elif (args.deploy == "loop"):
        loopDeploy()

if __name__ == "__main__":
    main(parseArgs())
