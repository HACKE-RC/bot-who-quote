from os import environ
import tweepy
import json
import random
import time

auth = tweepy.OAuthHandler(environ['key1'], environ['key2'])
auth.set_access_token(environ['key3'], environ['key4'])

api = tweepy.API(auth,
                    wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)

done = []

quotes = json.loads(open("quotes.json").read())

for _ in range(1643):
    nth = random.randint(0,1642)
    if nth not in done:
        done.append(nth)
        quote = quotes[nth]["text"]+" - "+quotes[nth]["author"]
        print(quote+"\n")
        api.update_status(quote)
        time.sleep(1000)