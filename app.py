# encoding=utf-8
import ConversationTemplate
import FlightConversationTemplate
import random
import re
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import os,sys
from flask import Flask,request
from pymessenger import Bot
PAGE_ACCESS_TOKEN="EAAd0eM695MABAHh4NfOlU7ZBFIZC1O1W9VqVBPDaPp9LuOPWWXn9h3RZB0pUFoZBrM9nqynOVCnRN5gAigZCdf8ik1uBzIbItbHApVYsEzKNpDyucxi3fDpbiWa5oG71DTDulMnfQ1x5ZAH5jxACZAQ3CyQiW5XZCazpgyZAO9z9rVgZDZD"
bot=Bot(PAGE_ACCESS_TOKEN)
app=Flask(__name__)
fi=FlightConversationTemplate.flight_info()

@app.route('/',methods=['GET'])
def verify():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"],200
    return "Hello world",200

@app.route('/',methods=['POST'])
def webhook():
    data=request.get_json()
    #log(data)

    if data['object']=='page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id=messaging_event['sender']['id']
                recipient_id= messaging_event['recipient']['id']
                if messaging_event.get('message'):
                    if('text' in messaging_event['message']):
                        messaging_text=messaging_event['message']['text']
                    else:
                        messaging_text='no_text'
                    response=ConversationTemplate.bot_respond(str(messaging_text),fi)
                   # response=messaging_text
                    bot.send_text_message(sender_id,response)
    return  "ok",200
def log(message):
    print(message)
    sys.stdout.flush()

if __name__=="__main__":
    ConversationTemplate.load_data()
    app.run(debug=True,port=80)


