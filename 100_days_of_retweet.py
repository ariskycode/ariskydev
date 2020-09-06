import tweepy
import time

print("It begins here")

auth = tweepy.OAuthHandler("aa", "bb")
auth.set_access_token("cc", "dd")
api = tweepy.API(auth)

def get_last_retweeted():
	return api.get_status(api.home_timeline()[0].in_reply_to_status_id_str).id_str

print(api.home_timeline()[0])

lastTweetCreatedAt = get_last_retweeted()
print (lastTweetCreatedAt)
for tweet in tweepy.Cursor(api.search, q="#100Days100Repos", count=100, lang="en", since_id=lastTweetCreatedAt).items(100): 
	print(" ----------------------------  ")
	print (tweet.user.screen_name, tweet.created_at, tweet.text, tweet.retweeted)

	lastTweetCreatedAt = tweet.created_at
	# api.retweet(tweet.id)
	# api.update_status('#100Days100Repos back to you! ' + '@' + tweet.user.screen_name, tweet.id)

print("It ends here")