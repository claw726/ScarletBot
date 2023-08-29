# ScarletBot

This Python script operates a GroupMe bot that post messages to a specified groupme chat.

Once the admin adds in the proper tokens and edits the messages, the script only needs to be ran when new messages need to be released.

I would reccomned using crontab to release the messages in a consistent time weekly or whatever your use case may be.

If you are interested in learning how to use crontab, here's a beginner's guide on how to set it up: https://linuxhandbook.com/crontab/

## Requirements
 - Python Installation with _requests_ installed

## How to use
 - Go to https://dev.groupme.com/bots and create a bot in the chat you want the bot in.
 - Copy the bot ID to the variable _access_token_
 - Copy the chat ID to the variable _group_id_
 - Run the program by running ``python -u ScarletBot.py`` in your console/terminal. (replace ``python`` with the appropriate command for your installation)
     
