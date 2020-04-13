# Easy Tweet Deleter

A simple app to delete tweets from a twitter account

# Get Your Keys!

1. You need a Twitter dev account: https://developer.twitter.com/en/apps, set up a Twitter developer account, and create an "App".  This contains 2 consumer API keys:
    - account_key
    - account_secrect

2. API access tokens for your twitter account from https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.  This contains 2 more API keys:
    - access_key
    - access_secret
    - 
# Instructions:

Easy Tweet Deleter contains 2 functions to check and to delete tweets, both require the same 6 parameters.
When checking tweets it is possible to list them to a text file with the optional 'text_file' parameter.
- username (str) = the twitter username
- account_key (str) = account_key from Step 1
- account_secret (str) = account_secret from Step 1
- access_key (str) = access_key from Step 2
- access_secret (str) = access_secret from Step 2
- date_older_than (str) = It will identify tweets before this date (use YYYY_MM_DD date format)

# Check Tweets
Use the function 'check_easy_twitter_deleter' to find and list tweets. 
It is reccomended that this is run first as when tweets are deleted they cannot be reteived!
~~~~python
import easy_tweet_deleter

username = "Username"
account_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
account_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
date_older_than = "2020-01-01"
text_file = "filepath"

easy_tweet_deleter.check_easy_twitter_deleter(username, account_key, account_secret, access_key, access_secret, date_older_than, text_file)
~~~~

# Delete Tweets
Use the function 'run_easy_twitter_deleter' to find and delete tweets
~~~python
import easy_tweet_deleter

username = "Username"
account_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
account_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
date_older_than = "2020-01-01"

easy_tweet_deleter.run_easy_twitter_deleter(username, account_key, account_secret, access_key, access_secret, date_older_than)
~~~
# easy_tweet_deleter
