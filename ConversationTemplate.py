#!/usr/bin/python3
# encoding=utf-8
from importlib import reload

from idna import unicode

import GhurboFlight
import random
import re
import sys
import datetime
import FlightConversationTemplate
reload(sys)
#sys.setdefaultencoding('utf-8')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////


bot_template = "BOT : {0}"
user_template = "USER : {0}"
bot_welcome=" ghurbo.com এ আপনাকে স্বাগতম\nআমি, ghurbo bot\nট্রাভেলিং সংক্রান্ত যে কোন কিছু আমাকে জিজ্ঞেস করতে পারেন"
bot_sorry="দুঃখিত বুঝতে পারি নি :( , দয়া করে খুলে বলবেন?"
unflexible_with_sites=[]
customer_addressing=[]#["শুভ অপ্রাহ্ন", "শুভ সন্ধ্যা","শুভ স্কাল", "ধ্ন্যবাদ"];
wh_question=[]#["কোথায়", "কখন", "কিভাবে","কেন","কেমন","কি","কে","কিরকম","কিধরনের","কিজন্য","কিকারনে","কিকরে"]

flight_start_done=0
flight_query=[]
customer_query=[]
query_type=["greetings","wh_question","other_question","information","other","yes_no_q"]
greeting_responses={
    "হ্যালো":customer_addressing,
    "হায়":customer_addressing,
    "hi":customer_addressing,
    "hello":customer_addressing,
    "শুভ অপ্রাহ্ন":customer_addressing,
    "শুভ সন্ধ্যা":customer_addressing,
    "শুভ সকাল":customer_addressing,
    "ধ্ন্যবাদ":customer_addressing
}
def find_if_there(list_name,message):
    for entry in list_name:
        m= re.search(entry,message)
        if m is not None:
            #print("yes.........")
            return True
    return False

def add_list_data(query_list,filename,):
    f= open(filename,encoding='utf-8',mode="r")
    lines=f.readlines()
    for line in lines:
        a=""
        for c in line:
            if(c=='\n'):
                break;
            a+=c
        query_list.append(a)

def load_data():
    add_list_data(wh_question,"wh_question.txt")
    add_list_data(customer_addressing, "addressing.txt")
    add_list_data(GhurboFlight.flight_query,"customer_query\\flight_query.txt")
    add_list_data(unflexible_with_sites,"customer_query\\unflexible_with_sites.txt")

def flight_conversation(message):
    a=1

def bot_respond(message,fi):
    message=message.lower()
    if find_if_there(unflexible_with_sites,message)==True:
        # string = GhurboFlight.detect_flight_query(message)
        # if string!="":
        #     string=GhurboFlight.ask_info
        #     print (GhurboFlight.ask_info)
        #     return unicode(string)
       #### string=GhurboFlight.ask_info
        fi.id=0
        string = FlightConversationTemplate.ask_info.__getitem__(0)
        return unicode(string)
    print (fi.departure)
    if fi.id==0 and FlightConversationTemplate.detect_place(message)!=fi.departure and fi.departure!="":
        string=FlightConversationTemplate.ask_info.__getitem__(2)
        return string
    if fi.id==0 and FlightConversationTemplate.detect_place(message) is not None:
        string = FlightConversationTemplate.ask_info.__getitem__(1)
        fi.departure=FlightConversationTemplate.detect_place(message)
        return unicode(string)


    if message in greeting_responses:
        hour = datetime.datetime.now().hour
        print(hour)
        if(hour>6 and hour<12):
            string=greeting_responses[message].__getitem__(0)
        elif (hour>=12 and hour<18):
            string=greeting_responses[message].__getitem__(1)
        elif hour>=18 and hour <20:
            string=greeting_responses[message].__getitem__(2)
        else:
            string=greeting_responses[message].__getitem__(3)
        string=string+bot_welcome
        reply=unicode(string)
        return reply
    string=GhurboFlight.detect_flight_query(message)
    if(string!=""):
        return unicode(string)
    string=bot_sorry
    return unicode(string)


# responses = {
#     "what is your name?": "my name is ghurbo bot",
#     "hi": "hello",
#     "হ্যালো আমি ঘুরতে যেতে চাই" : "আপনি কোথায় ঘুরতে যেতে চান?",
#     "কেমন আছ*" : [
#                     "ভাল",
#                     "মোটামুটি",
#                     "খারাপ"
#                  ],
#
# }
