import requests

# Replace with your GroupMe API access token
access_token = "API_TOKEN"
# Replace with the group ID of the group you want to send the message to
group_id = "GROUP_ID"
# Replace with the message you want to send
messages = ["""Hope you all had a great Week!
If you'd like a ride to Calvary this Sunday to either the 8:15, 9:45 or 11:15 service, please like the appropriate message and show up to the 507 at 7:45/9:15/10:45 respectively. We will leave at 7:55/9:25/10:55 respectively.
            
If you need to be picked up from another location, feel free to message a driver to pick you up. Keep in mind that for each like a driver gives in a time slot, 4 people can be driven to said service.
            
If a driver cannot make it to a specific service time, we cannot guarentee a ride to that service, and I reccomend you go to another service that has drivers.
            
If no drivers are available or you cannot make it to a service, Calvary will have an online service you may attend: https://yourcalvary.info/livestream""",

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"Like this message if you need a ride to the 8:15 service at Calvary (leave at 7:55). 🙋",

"Like this message if you can drive others to the 8:15 service at Calvary. 🚗",

"Like this message if you need a ride to the 9:45 service at Calvary (leave at 9:25). 🙋", 

"Like this message if you can drive others to the 9:45 service. 🚗", 

"Like this message if you need a ride to the 11:15 service at Calvary (leave at 10:55). 🙋",

"Like this message if you can drive others to the 11:15 service. 🚗"]

def send_messages():
    for message in messages:
        post_main_message(message)

def post_main_message(message):
    url = f"https://api.groupme.com/v3/bots/post?token={access_token}"
    data = {"bot_id": group_id, "text": message}
    requests.post(url, json=data)

send_messages()
