import time
import tweepy

# Constants
API_KEY = ""
API_KEY_SECRET = ""
BEARER_TOKEN = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""


def getIDs(client):
    # get user id - needed for future API requests
    userID = client.get_user(username="username")[0]['id']
    return userID


def unlikeTweets(userID):
    global count
    # get my liked tweets
    likedTweets = client.get_liked_tweets(userID)[0]
    #loop through tweets
    try:
        for likedTweet in likedTweets:
            count += 1
            if count % 10 == 0:
                print(f"Unliked a total of {count} tweets")
            client.unlike(likedTweet['id'])
    except:
        count -= 1
        print(f"50 Requests per 15 minutes limit has been reached. Pausing for 15 minutes. {time.strftime('%H:%M:%S', time.localtime())}")
        time.sleep(900)
        return False
    print("done")
    return True

if __name__ == "__main__":
    # Set up auth and api by using a generated Beaerer token
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        consumer_key=API_KEY,
        consumer_secret=API_KEY_SECRET,
    )
    done = False
    clientId = getIDs(client)
    count = 0
    print("unliking all tweets....")
    while not done:
        try:
            done = unlikeTweets(clientId)
        except:
            time.sleep(30)