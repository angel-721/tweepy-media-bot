# tweepy-media-bot
A simple twitter media sharing bot implemented in Python using the [Tweepy module](https://www.tweepy.org/).<br>
[One bot deployed with this](https://twitter.com/omoriupscalebot)

### Use
- Install dependencies with <code> pip install -r requirements.txt</code>
- Make a [Twitter developer](https://developer.twitter.com/en) account. Put your account keys in <code>./textfile/keys.txt</code>, then deploy using a method of your choice :) <br>
The filenames script can be used to automate making a medialist.txt file needed for the bot to upload images. 



### Deployment methods: 
- Use a [AWS](https://aws.amazon.com/) server to host the bot and run the main.py every hour. One such way is to use a cronjob that runs at the start of every hour.
- Another method is to comment out the first Bot and use an infinite loop that uses the time.sleep() function to wait every hour. 
