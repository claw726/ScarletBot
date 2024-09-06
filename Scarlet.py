from dotenv import load_dotenv
import os
import requests
import logging

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# load environment vars from .env file
load_dotenv()


# Modify tokens in .env file in the below format:
# KEY=VALUE

# Ex:
# ACCESS_TOKEN=randomstring194553925489

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CALVARY_GROUP_ID = os.getenv("CALVARY_GROUP_ID")
DEBUG_GROUP_ID = os.getenv("DEBUG_GROUP_ID")

# Base URL for GroupMe API
BASE_URL = f"https://api.groupme.com/v3/bots/post?token={ACCESS_TOKEN}"


# Replace with the message you want to send
messages = ["""Hope you all had a great Week!
If you'd like a ride to Calvary this Sunday to either the 8:15, 9:45 or 11:15 service, please like the appropriate message and show up to the 507 at 7:45/9:15/10:45 respectively. We will leave at 7:55/9:25/10:55 respectively.
            
If you need to be picked up from another location, feel free to message a driver to pick you up. Keep in mind that for each like a driver gives in a time slot, 4 people can be driven to said service.
            
If a driver cannot make it to a specific service time, we cannot guarentee a ride to that service, and I reccomend you go to another service that has drivers.
            
If no drivers are available or you cannot make it to a service, Calvary will have an online service you may attend: https://yourcalvary.info/livestream.
            
Questions or concerns? Text Charles Law at (317) 741-6034.""",

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"Like this message if you need a ride to the 8:15 service at Calvary (leave at 7:55). 🙋",

"Like this message if you can drive others to the 8:15 service at Calvary. 🚗",

"Like this message if you need a ride to the 9:45 service at Calvary (leave at 9:25). 🙋", 

"Like this message if you can drive others to the 9:45 service. 🚗", 

"Like this message if you need a ride to the 11:15 service at Calvary (leave at 10:55). 🙋",

"Like this message if you can drive others to the 11:15 service. 🚗",

"Like this message if you need a ride to College at Calvary. (Meet after Sunday Supper at 8:00 PM). 🙋",

"Like this message if you can drive others to College at Calvary. Leave no later than 8:15 PM 🚗" ]

debug_messages = ["DEBUG MESSAGE"]

def send_messages(group_id, messages):
    # send messages to the specified GroupMe group
    for message in messages:
        post_message(group_id, message)


def post_message(group_id, message):
    # post a single message to GroupMe
    data = {"bot_id": group_id, "text": message}
    try:
        response = requests.post(BASE_URL, json=data)
        response.raise_for_status() # Raise an exception for HTTP errors
        logging.info(f"Message sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message: {message}. Error: {e}")

def post_debug_message(debug_message):
    url = f"https://api.groupme.com/v3/bots/post?token={access_token}"
    data = {"bot_id": debug_group_id, "text": debug_message}
    requests.post(url, json=data)

# Send Main messages
send_messages(CALVARY_GROUP_ID, messages)

# Send debug messages (comment if unneeded)
# send_messages(DEBUG_GROUP_ID, debug_messages)
