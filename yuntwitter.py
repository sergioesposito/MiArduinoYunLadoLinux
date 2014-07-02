#!/usr/bin/python
from twython import Twython
import sys
OAUTH_TOKEN='xxx'
OAUTH_TOKEN_SECRET='xxx'
messagetotwitter=sys.argv[1]
APP_KEY='xxx'
APP_SECRET='xxx'
twitter=Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status=messagetotwitter)
