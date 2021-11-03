import praw
import re
import time

reddit = praw.Reddit(client_id='ND9KfaajIk6cUs57G0IwdQ',  # this passes in my data
                     client_secret='AFLQV3X3TOthlfxblz1ZtLVdov0EVw',
                     user_agent='< console: name: Lex_Fridman_Bot version 0.0.1 (by / u /Due-Soft8913) >',
                     redirect_uri="http://localhost:8080",
                     username='Due-Soft8913',
                     password='123546yecS!')

print(reddit.auth.url(["identity"], "...", "permanent"))
# # this sets up my connection to reddit's API
# # Need to create a new reddit account

# # print(reddit.read_only)

# subreddits = ['lexfridman, samharris']
# pos = 0

# title = "I am a Lex Fridman bot"
# url = "https://lexfridman.com/"


# def post():
#     global subbreddits
#     global pos

#     # this makes sure I hit the correct subreddit
#     subreddit = reddit.subreddit(subreddits[pos])
#     subreddit.submit(title, url=url)

#     pos = pos + 1     # adjusts for position in subreddit array

#     if (pos >= len(subreddits) - 1):
#         post()
#     else:
#         print("Done")


# post()
