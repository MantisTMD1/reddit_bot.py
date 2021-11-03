import praw
import re
import time

reddit = praw.Reddit(client_id='TX0T6V1mevTgnZ-PT_CW4A',  # this passes in my data
                     client_secret='-Ih7uA-shjiGkDORbdXdivawX2vJug',
                     user_agent='< console: name: Lex_Fridman_Bot version 0.0.1 (by / u /Due-Soft8913) >',
                     redirect_uri="http://localhost:8080",
                     username='Due-Soft8913',
                     password='123546yecS!')

# print(reddit.auth.url(["identity"], "...", "permanent"))
# this sets up my connection to reddit's API
# Need to create a new reddit account


subreddits = ['lexfridman', 'samharris', 'JordanPeterson']
pos = 0

title = "I am a Lex Fridman bot" #what my bot will post 
url = "https://lexfridman.com/"


def post(): #method to post onto subreddits
    global subbreddits
    global pos

    subreddit = reddit.subreddit(subreddits[pos])
    subreddit.submit(title, url=url)

pos = pos + 1   # adjusts for position in subreddit array
post()

#parses through subreddits in array I created
if (pos <= len(subreddits) - 1):
    post()
else:
    print("Done")
post()
