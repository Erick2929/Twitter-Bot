import tweepy
import time

apiKey = "Here goes the key"
apiKeySecret = "Here goes the key"

accessToken = "Here goes the key"
accessTokenSecret = "Here goes the key"


print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#mentions = api.mentions_timeline()
#followers = api.get_followers()



lastMentionsAmount = 'lastSeenTweet.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)

    #establecemos el ultimo tweet que analizamos
    lastMsAmount = retrieve_last_seen_id(lastMentionsAmount)

    #accesamos la timeline desde el ultimo tweet que analizamos
    mentions = api.mentions_timeline()
    followers = api.get_follower_ids()

    updatedMsAmount = len(mentions)
    #analizamos las menciones
    if lastMsAmount < updatedMsAmount:

        print(str(mentions[0].id) + ' - ' + mentions[0].text, flush=True)
        lastMsAmount = updatedMsAmount
        store_last_seen_id(lastMsAmount, lastMentionsAmount)

        if '#dm' in mentions[0].text.lower():
            if mentions[0].user.id in followers:
                print('found a user mention', flush=True)
                print('responding back...', flush=True)
                api.send_direct_message(mentions[0].user.id,
                "Hola , en que te puedo ayudar??")

        elif '#tagme' in mentions[0].text.lower():
            api.update_status('@' + mentions[0].user.screen_name +
            " Hey there!!")

while True:
    reply_to_tweets()
    time.sleep(120)