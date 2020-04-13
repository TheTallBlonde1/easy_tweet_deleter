import os
import twitter
import GetOldTweets3 as got
from datetime import datetime, timedelta

class Easy_Twitter_Deleter:
    def __init__(self, username, account_key, account_secret, access_key, access_secret, date_older_than):
        self.username = str(username)
        self.account_key = str(account_key)
        self.account_secret = str(account_secret)
        self.access_key = str(access_key)
        self.access_secret = str(access_secret)

        if type(date_older_than) == str:
            self.datetime_older_than = datetime.strptime(date_older_than,"%Y-%m-%d")
        elif isinstance(date_older_than, datetime.date):
            self.datetime_older_than = date_older_than

        self.twitter_api = twitter.Api(self.account_key, self.account_secret, self.access_key, self.access_secret, sleep_on_rate_limit=True, use_gzip_compression=True)
        self.twitter_api.VerifyCredentials()
        self.tweets_to_delete = []

        
    def get_tweets_to_delete_got_method(self):
        years = self.get_years_to_now(self.datetime_older_than.year)
        for yr in years:
            date_until = self.get_got_date_until(yr)
            if date_until:
                tweetCriteria = got.manager.TweetCriteria().setUsername(self.username).setSince("{}-01-01".format(yr)).setUntil(date_until).setMaxTweets(-1)
                tweets = got.manager.TweetManager.getTweets(tweetCriteria)
                for tweet in tweets:
                    self.add_to_tweets_to_delete(tweet, self.get_got_date_time(tweet.formatted_date))

    def get_tweets_to_delete_api_method(self):
        last_min_id = None
        while True:
            tweets = self.twitter_api.GetUserTimeline(include_rts=True,exclude_replies=False,max_id=last_min_id,count=10)
            if len(tweets) == 0:
                break
            for tweet in tweets:
                self.add_to_tweets_to_delete(tweet, datetime.utcfromtimestamp(tweet.created_at_in_seconds))
                last_min_id = self.get_last_min_id(tweet, last_min_id)

    def add_to_tweets_to_delete(self, tweet, created_at_datetime):
        if created_at_datetime < self.datetime_older_than:
            if not any(x.id == tweet.id for x in self.tweets_to_delete):
                self.tweets_to_delete.append(Tweet_Idenifier(tweet.id, tweet.text, created_at_datetime))

    @staticmethod
    def get_last_min_id(tweet, last_min_id):
        if last_min_id:
            last_min_id = min([tweet.id - 1, last_min_id])
        else:
            last_min_id = tweet.id - 1
        return last_min_id

    def list_tweets(self):
        if not self.tweets_to_delete:
            print("No tweets found")
            return
        print("Number of tweets identified (before {0}) {1}".format(self.datetime_older_than.strftime("%Y-%m-%d"), len(self.tweets_to_delete)))
        if self.tweets_to_delete:
            for tweet in self.tweets_to_delete: 
                print("{0} {1}".format(" ".join(tweet.text.splitlines()), tweet.date))

    def delete_tweets(self):
        if not self.tweets_to_delete:
            print("No tweets found")
            return
        print("Number of tweets to delete (before {0}) {1}".format(self.datetime_older_than.strftime("%Y-%m-%d"), len(self.tweets_to_delete)))
        if self.tweets_to_delete:
            for tweet in self.tweets_to_delete: 
                try:
                    self.twitter_api.DestroyStatus(tweet.id)
                    print("Tweet Deleted:  {0} {1}".format(" ".join(tweet.text.splitlines()), tweet.date))
                except:
                    print("Could not delete {0} {1}".format(" ".join(tweet.text.splitlines()), tweet.date))


    def get_got_date_until(self, yr):
        if yr == self.datetime_older_than.year:
            d = self.datetime_older_than - timedelta(days=1)
            if yr != d.year:
                return None
            else:
                return d.strftime("%Y-%m-%d")
        else:
            return "{}-12-31".format(yr)

    @staticmethod
    def get_years_to_now(to_year=None):
        if not to_year:
            to_year = datetime.now().year
        yr = 2006
        years = []
        while True:
            years.append(yr)
            yr += 1
            if yr > to_year:
                break
        return years

    @staticmethod
    def get_got_date_time(input_value):
        return datetime.strptime(f"{input_value[-4:]}-{input_value[4:7]}-{input_value[8:10]}","%Y-%b-%d")

    def create_check_text_file(self, text_file):
        if not self.tweets_to_delete:
            return
        if text_file:
            if os.path.exists(text_file):
                os.remove(text_file)
            try:
                with open(text_file, "w", encoding="utf-8") as fs:
                    fs.write("tweet id\ttweet text\ttweet date\n")
                    for tweet in self.tweets_to_delete: 
                        fs.write("{0}\t{1}\t{2}\n".format(tweet.id, " ".join(tweet.text.splitlines()) , tweet.date))
            except:
                print("Cannot create text file {}".format(text_file))

class Tweet_Idenifier:
    def __init__(self, id_num, text, date):
        self.id = str(id_num)
        self.text = str(text)
        self.date = date

def run_easy_twitter_deleter(username, account_key, account_secret, access_key, access_secret, datetime_older_than):
    """
    Use the function 'run_easy_twitter_deleter' to find and delete tweets
    """
    app = Easy_Twitter_Deleter(username, account_key, account_secret, access_key, access_secret, datetime_older_than)
    app.get_tweets_to_delete_api_method()
    app.get_tweets_to_delete_got_method()
    app.delete_tweets()

def check_easy_twitter_deleter(username, account_key, account_secret, access_key, access_secret, datetime_older_than, text_file=None):
    """
    Use the function 'check_easy_twitter_deleter' to find and list tweets.

    It is reccomended that this is run first as when tweets are deleted they cannot be reteived!
    """
    app = Easy_Twitter_Deleter(username, account_key, account_secret, access_key, access_secret, datetime_older_than)
    app.get_tweets_to_delete_api_method()
    app.get_tweets_to_delete_got_method()
    app.list_tweets()
    if text_file:
        app.create_check_text_file(text_file)


