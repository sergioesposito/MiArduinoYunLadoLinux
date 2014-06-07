#!/usr/bin/python
from twython import Twython
import sys
OAUTH_TOKEN='78294886-6yO08xifX5Pg87Ra5GkNbDiu4hHf1qnseA2bHu3s2'
OAUTH_TOKEN_SECRET='2OkHVL4ngFCETEaB32upjJm2FmSjYUqfpYCdcD9mTdwDM'
messagetotwitter=sys.argv[1]
APP_KEY='ytDXIzPZacr4PS8lbAbBqHcBt'
APP_SECRET='6lCrwnJMqNz39dFcP9VRdfujsrpZKiZhRV82Zm39Rh943NQGub'
twitter=Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status=messagetotwitter)
