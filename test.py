import praw
import re
import time

reddit = praw.Reddit(client_id='ND9KfaajIk6cUs57G0IwdQ',  # this passes in my data
                     client_secret='AFLQV3X3TOthlfxblz1ZtLVdov0EVw',
                     user_agent='< console:name: Lex_Fridman_Bot version 0.0.1 (by / u /Due-Soft8913) >',
                     username='Due-Soft8913',
                     password='123546yecS!')
# this sets up my connection to reddit's API
# Need to create a new reddit account

print(reddit.read_only)
