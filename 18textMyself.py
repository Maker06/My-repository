#! python3
# 18textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = 'AC3fea6e4e7e285b7b5d4b1c5760252da4'
authToken = '9e5a96026d653fbfb944a4ccdbb8f3e8'
myNumber = '+380976038100'
twilioNumber = '+14159496645'
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

textmyself('The boring task finished.')