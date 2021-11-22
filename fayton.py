import urllib.request
import json

name=input("Enter username: ")
key = 'AIzaSyBlOaaWs5iorKo0JcyiX3T8tu7zSyLf65c'

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + "{:,d}".format(int(subs)) + " subscribers")

