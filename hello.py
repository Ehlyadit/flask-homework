import requests
import os
from flask import Flask, request

#TOKEN = None
#with open("token.txt") as f:
#    TOKEN = f.read().strip()

TOKEN = os.environ["TOKEN"]
RENDER_URL = os.environ["RENDER_URL"]
print(TOKEN)

sendMessage = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

result = requests.post(rf"https://api.telegram.org/bot{TOKEN}/setWebhook", params={"url":RENDER_URL})
print("webhook", result)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/',methods = ['POST', 'GET'])
def echo():
    message = request.json
    requests.post(sendMessage, params={"chat_id":message["message"]["chat"]["id"], 
                                       "text":message["message"]["text"], 
                                       "reply_to_message_id":message["message"]["message_id"]})
    return message["message"]["text"]
