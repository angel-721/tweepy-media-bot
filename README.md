# tweepy-media-bot
A simple Twitter media sharing bot implemented in Python using the [Tweepy module](https://www.tweepy.org/).<br>

### WARNING
- Twitter's(X) new API is out and this doesn't work with APIV2 access points so you must make sure you are using APIV1.1 points
- I'm not sure but I can't find a way to get access to media end points with the new X API so this is the end of this project Twitter(X) changes the API policy

### Use
- Install dependencies with <code> pip install -r requirements.txt</code>
- Make a [Twitter developer](https://developer.twitter.com/en) account. Put your account keys in <code>./text-files/keys.txt</code>, then deploy using a method of your choice :) <br>
- Make sure that the tokens for the account have write access.
- populate the database by running <code> ./main.py -make-database 1 </code> - Run this everytime you add new images/gifs to the media folder.
- When running <code>main.py</code> make sure to include the argument <code>-deploy</code> to specify which deployment method you want. 
	- <code>-deploy cronjob</code> if you want to use a cronjob 
	- <code>-deploy loop</code> if you want to use an infinte loop

### Functions 
- Tweet with media
- Like mentions
- Tweet based off a keyword

### Deployment methods: 
- 1) Use a [AWS](https://aws.amazon.com/) server to host the bot and run the main.py every hour. One such way is to use a cronjob that runs at the start of every hour.
  - <code>runbot</code> script can help with this 
- 2) Another method is to comment out the first Bot and use an infinite loop that uses the time.sleep() function to wait every hour. 

### Example 
- <code>python main.py -deploy cronjob</code> 
- if you want to run the py file as a script you can also do <code>./main.py -deploy cronjob</code>
  - Make sure you have executable privileges for <code>main.py</code> if you want to run it as above. If not the first way works just fine! 
