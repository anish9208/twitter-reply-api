__author__ = 'anish'



import urllib
from pyquery import PyQuery as pq


def get_replyid(name,id):


     url = "https://twitter.com/"+name+"/status/"+id
     print url

     lone_tweet = []
     conversation= {}

     page = urllib.urlopen(url).read()

     #in page  variable  we  have  all  html  data  in  string  format






     count= 1
     d = pq(page) # from  here  on  d  will  work  like  $ in  jquery
     idarr = []
     alldiv=d(page).find("li.ThreadedConversation")
     for i in alldiv:

          divs = d(i).find("div.ThreadedConversation-tweet")
          con_tweet = []
          for j in divs:
               eachi = d(j).find("li")
               id = eachi[0].attrib['data-item-id']
               con_tweet.append(id)

          # below  code  is  note  needed  since  script  captures  all  element  which contains ThreadedConversation-tweet in  their  class name
          #which include ThreadedConversation-tweet last  tweet ... so  no seprate  code needed to fetch last  tweet  data

          # last = d(i).find("div.last")
          # each = d(last).find("li")
          # id = each[0].attrib["data-item-id"]
          # con_tweet.append(id)
          # print each

          conversation[count] = con_tweet
          count+=1
          idarr.append(conversation)

     # till  this  point  we  are  getting  data  from ThreadedConversation-tweet
     #each  reply  tweet  is  added  to conversation object   with  it's  group  value  as  key



     d = pq(page)
     alldiv=d(page).find("div.ThreadedConversation--loneTweet")
     for i in alldiv:
          a = d(i).find("li")
          id = a[0].attrib['data-item-id']
          lone_tweet.append(id)


     #here we  have  all  loneTweet data  in  arry  lone_tweet  and  we  will  insert  this  arry
     #with  key '0' (i.e. group  0 ) in conversation  object

     conversation[0] = lone_tweet

     #print conversation
     return conversation



# these  are  all  commented    section so  no  need  to  look  into  it  if  are  finiding  any  error  in  program

#below is  jquery  script  which  i  tried  to replicate  in code  above

# function findReplyConversations(body) {
# 			var id;
# 			var idArr = [];
# 			var allli = $(body).find("li.ThreadedConversation");
#
# 			for (var i = 0; i < allli.length; i++) {
# 				console.log($(allli[i]));
# 				var divs = $(allli[i]).find("div.ThreadedConversation-tweet");
# 				var conversation = {};
# 				var con_tweets = [];
# 				for (var j = 0; j < divs.length; j++) {
# 					var eachLi = $(divs[j]).find("li");
# 					id = eachLi[0].attributes[1].nodeValue;
#
# 					con_tweets.push(id);
#
# 					//console.log(id);
# 				}
# 				var last = $(allli[i]).find("li.last");
# 				var each = $(last).find("li");
# 				var ids = eachLi[0].attributes[1].nodeValue;
# 				con_tweets.push(id);
# 				conversation[i+1]=con_tweets;
# 				idArr.push(conversation);
#
# 			}
# 			return idArr;
# 		}
#

#these  are  two  sample  urls

# https://twitter.com/Swamy39/status/727520502412136448
# https://twitter.com/FoxNews/status/729356516130574337

# un comment  this code  if  you  want  to  run  this  file  alone

# un = "Swamy39"
# twt = "727520502412136448"
# #print soup.prettify('latin-1')
# get_replyid(un,twt)

