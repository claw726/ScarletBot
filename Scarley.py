import requests
import datetime

# Replace with your GroupMe API access token
access_token = ""
# Replace with the group ID of the group you want to send the message to
group_id = ""
# Replace with the message you want to send
messages = ["Hope you all had a great Week! If you'd like a ride to church this Sunday to either the 8:15, 9:45 or 11:15 service, please like the appropriate message and show up to the house at 7:45/9:15/10:45 respectively. We will leave at 7:55/9:25/10:55 respectively. If you need to be picked up from another location, feel free to message a driver to pick you up. Keep in mind that for each like a driver gives in a time slot, 4 people can be driven to said service. If a driver cannot make it to a specific service time, we cannot guarentee a ride to that service, and I reccomend you go to another service that has drivers. If no drivers are unavailable, Calvary will have an online service you may attend: [URL]",
"Like this message if you need a ride to the 8:15 service (leave at 7:55).",
"Like this message if you can drive others to the 8:15 service.",
"Like this message if you need a ride to the 9:45 service(leave at 9:25).", 
"Like this message if you can drive others to the 9:45 service.", 
"Like this message if you need a ride to the 11:15 service(leave at 10:55).",
"Like this message if you can drive others to the 11:15 service."]

def send_messages():
    for message in messages:
        post_main_message(message)

def post_main_message(message):
    url = f"https://api.groupme.com/v3/bots/post?token={access_token}"
    data = {"bot_id": group_id, "text": message}
    requests.post(url, json=data)

send_messages()
