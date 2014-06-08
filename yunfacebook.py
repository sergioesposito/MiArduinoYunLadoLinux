#!/usr/bin/python
import facebook
import sys
messagefacebook=sys.argv[1]
graph = facebook.GraphAPI('CAAURY73RwKcBAHrZAHBWZB8ADWWXfXmZBdR9xKZC4k1ZBK5xGZCWybc1FuLlALibJDAnv68efT0QP9h77REpCerNNjMNpKMIHWbRzQNBihU036iBdLqvgpBXbiE37TTRZA3ZC8y05bdqzrwu8q3sPgSkpJvIZBpaQ4yrrlcAuTrXnfGYlL9bhdxBoBMhnw7O4zC8ZD')
graph.put_object("me", "feed", message=messagefacebook)