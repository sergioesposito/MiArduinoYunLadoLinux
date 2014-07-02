#!/usr/bin/python
import facebook
import sys
messagefacebook=sys.argv[1]
graph = facebook.GraphAPI('xxx')
graph.put_object("me", "feed", message=messagefacebook)
