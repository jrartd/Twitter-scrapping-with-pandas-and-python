import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret) 
api = tweepy.API(auth)


results = []
#Keyword to search
keyword = "#RealMadrid"
for tweet in tweepy.Cursor(api.search, q=keyword).items(500):
    results.append(tweet)
    
def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])

    # Processing Tweet Data

    data_set["text"] = [tweet.text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]

    # Processing User Data
    data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    data_set["profile_image_url"] = [tweet.author.profile_image_url_https for tweet in results]
    data_set["url_destino"] = [tweet.author.url for tweet in results]

    return data_set
data_set = process_results(results)
data_set["created_at"] = pd.to_datetime(data_set["created_at"])
data_set.head()
