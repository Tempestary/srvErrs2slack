# -*- coding: utf-8 -*-
import sys, re
from slacker import IncomingWebhook

def exception_search():
    reg = re.compile(r'Exception : System.Exception: ')
    ExceptionsList = []
    reg_body = re.compile(r'^[- ]')
    while True:
        try:
            line = sys.stdin.readline()
            result2 = reg_body.search(line)
            #check if our exception does have a body to show (as we're only looking for those)
            if len(ExceptionsList)>0:
                if result2 != None:
                    ExceptionsList.append(line.rstrip())
                else:
                    yield ExceptionsList
                    ExceptionsList = []
            #check if the line we're bumped into really is the first line of an exception and not something from the stack trace
            if len(ExceptionsList) == 0:
                result = reg.search(line)
                if result != None:
                    ExceptionsList.append(line.rstrip())
                #print(ExceptionsList)
        except KeyboardInterrupt:
            break 

def send_slack_message(slack: IncomingWebhook, channel: str, message: str, icon: str = ':thinking_face:'): #you're free to use any emojii icon you like here

    payload = {
        'channel': channel,
        'username': 'MyBot', #add desired bot name here
        'icon_emoji': icon, #configure the icon above or use my default
        'text': message
    }

    slack.post(payload)

def main():
    slack = IncomingWebhook(url='#PasteYourSlackWebhookHere')
    
    for exception in exception_search():
        if len(exception) > 1:
            traceback = "\n".join(exception)
            send_slack_message(slack, "#your_slack_channel_here", "```"+" "+traceback+" "+"```", ":thinking_face:")


if __name__ == '__main__':
    main()
