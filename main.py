#!/usr/bin/python
"""
Main file that calls the helper methods to delpy the bot.

Make sure if you don't have a ./pyfiles/image.db file run the make-database.
command before trying to tweet!
"""
import argparse
from time import sleep

from pyfiles.botmethods import Bot
from pyfiles.database import populateTable

bot = Bot()


def cronJobDeploy():
    """USE THIS IF USING A CRONJOB TO DEPLOY."""
    bot.makeTweet()


def loopDeploy():
    """USE THIS IF USING A INFINTE LOOP TO DEPLOY."""
    running = True
    while running:
        bot.makeTweet()
        # 3600 seconds = 1 hour
        sleep(3600)


def parseArgs():
    """Parse cli arguments mainly for getting the type of deployment."""
    parser = argparse.ArgumentParser(
        prog='Tweepy-Media-Bot',
        description='Tweets and Likes Media in a automated fasion',
    )
    parser.add_argument('-deploy', choices=('cronjob', 'loop'))
    parser.add_argument('-make-database', type=int, default=0)
    args = parser.parse_args()
    return args


def main(args):
    """Handle the command line args and call functions."""
    if args.deploy == 'cronjob':
        cronJobDeploy()
    elif args.deploy == 'loop':
        loopDeploy()
    if args.make_database != 0:
        populateTable()


if __name__ == '__main__':
    main(parseArgs())
