__author__ = 'anish'



import tweepy
from url_scrap import get_replyid
import json

# Consumer keys and access tokens, used for OAuth
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# code  below  reads  text  from  file  input_file.txt and  stores that  string  it  in search query  variable

f = open("input_file.txt" , "r")
search_query = f.read()

# line  below  calls  search  api  of  twitter  and  gets  data  in  form of  array  of  15  tweets
#each  tweet as  json object

st =  api.search(q=search_query , lang ='en')

sts = ''

a  = dict()

# here  in dictionary (json object in python) we  are  storing  id , text ,  handle of  user who tweeted
#and  hash tags  mentioned  in  the  tweet

for  i in range(0,len(st)):
    a[i]= [st[i].__dict__['id'],st[i].__dict__['text'] ,st[i].__dict__['author'].__dict__['screen_name'] , st[i].__dict__['_json']['entities']['hashtags']]

print a


big_ary = []
for  tw  in  a  :
    tmp = []
    ar = get_replyid(str(a[tw][2]),str(a[tw][0]))
    for i in ar.keys():
        for j in ar[i]:
            sts=api.get_status(j)
            tmp.append({"id":sts.__dict__['id_str'],"text":sts.__dict__['text'] , "group" :i})
    sts2 = api.get_status(a[tw][0])
    big_ary.append({"par_tweet_text":sts2.__dict__['text'] , "par_tweet_id":a[tw][0] ,"reply":tmp})



print big_ary

obj = json.dumps({'data':big_ary})

f = open("result.json","w")
f.write(obj)
f.close()











































#st2 = st[0].__dict__['author']
#print st2.__dict__.keys()

# f=file("out.json","w")
# f.write(sts)
# f.close()


# import requests
#
# url = "https://twitter.com/RCGameforLife/status/720601711304253441"
#
# import urllib
# from lxml import html
#
# #url = "http://www.infolanka.com/miyuru_gee/art/art.html"
# page = urllib.urlopen(url).read()
#
# print page
