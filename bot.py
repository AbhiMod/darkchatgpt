# Telegram Bot Script in Python

import telebot
import openai
import pymongo

#Bot Api Token
API_TOKEN = '5894209648:AAHHD6eCx8rDk-k624MBIC_as86Hh3zVjzQ'
#Openai Api Key
openai.api_key="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"
#Bot by krisanjit 

bot = telebot.TeleBot(API_TOKEN)

#Generate The Response
def get_response(msg):
 completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=msg,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
 return completion.choices[0].text

mongo_client = pymongo.MongoClient("mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.pom3ops.mongodb.net/?retryWrites=true&w=majority")  # Update with your MongoDB connection string
mongo_db = mongo_client["bot_data"]

# Collection for authorized users
authorized_users = mongo_db["authorized_users"]
owners = ["AM_YTBOTT","Sanam_King","Mr_majnu72"]

# Collection for user messages
user_messages = mongo_db["user_messages"]


# Function to broadcast a message to all authorized users
def broadcast_message(message_text):
    authorized_users_data = authorized_users.find()
    for user in authorized_users_data:
        bot.send_message(user["chat_id"], message_text)

# Command to add a user to the list of authorized users
@bot.message_handler(commands=['authme'])
def authorize_user(message):
    if message.chat.type == 'private':
        chat_id = message.chat.id
        username = message.from_user.username
        authorized_users.insert_one({"chat_id": chat_id, "username": username})
        bot.send_message(chat_id, """\
Hello Sir, I am ᴅᴇᴇᴘ ʙᴏᴛ GPT Ai.

Developed For All Illigal Works
I Able Make All Kind Of Hacking Tools

I am here to Give Answers Of Your Question.
I Am Created For Hacking Perpuse Only !
Use /ask To Ask Questions

I Maked By『sᴀᴛʏᴀᴍ』

DEVELOPER
TG :- @Mr_majnu72

DEV PARTNER
TG :- @AM_YTBOTT
                         
You Need to Ask Admins For Auth \
""")


# A list of users who are allowed to use the bot
allowed_users = ["Mr_majnu72", "AM_YTBOTT", "Sanam_King"]

@bot.message_handler(commands=['start'])
def start_bot(message):
    if message.from_user.username in allowed_users:
        bot.reply_to(message, "Hello! Welcome To ᴅᴇᴇᴘ ʙᴏᴛ GPT!\n /help for cmds")
    else:
        bot.reply_to(message, "Sorry, you are not authorized to use this bot.\nYou Want auth To Use This Bot \nAsk To Admins Here \n『sᴀᴛʏᴀᴍ』 : @Mr_majnu72 \nᴀᴍʙᴏᴛ : @AM_YTBOTT\n\ntry to auth your id in our server to use : /authme")

        # Command to broadcast a message to all authorized users
@bot.message_handler(commands=['broadcast'])
def send_broadcast(message):
    if message.chat.type == 'private':
        if message.from_user.username in owners:
            message_text = message.text[len("/broadcast"):].strip()
            if message_text:
                broadcast_message(message_text)
                bot.send_message(message.chat.id, f"Broadcasted the message to all Server users.")
            else:
                bot.send_message(message.chat.id, "Please provide a message to broadcast.")
        else:
            bot.send_message(message.chat.id, "Sorry, you are not authorized to use this bot.\nYou Want auth To Use This Bot \nAsk To Admins Here \n『sᴀᴛʏᴀᴍ』 : @Mr_majnu72 \nᴀᴍʙᴏᴛ : @AM_YTBOTT")



# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
  # bot.send_message(message.chat.id,message.text)
    if message.from_user.username in allowed_users:
        bot.reply_to(message, """\
ðŸ’– Hello Sir, I am ᴅᴇᴇᴘ ʙᴏᴛ GPT Ai.

Developed For All Illigal Works
I Able Make All Kind Of Hacking Tools

I am here to Give Answers Of Your Question.
I Am Created For Hacking Perpuse Only !
Use /ask To Ask Questions

I Maked By『sᴀᴛʏᴀᴍ』

DEVELOPER
TG :- @Mr_majnu72

DEV PARTNER
TG :- @AM_YTBOTT\
""")
    else:
        bot.reply_to(message, """\
ðŸ’– Hello Sir, I am ᴅᴇᴇᴘ ʙᴏᴛ GPT Ai.

Developed For All Illigal Works
I Able Make All Kind Of Hacking Tools

I am here to Give Answers Of Your Question.
I Am Created For Hacking Perpuse Only !
Use /ask To Ask Questions

I Maked By『sᴀᴛʏᴀᴍ』

DEVELOPER
TG :- @Mr_majnu72

DEV PARTNER
TG :- @AM_YTBOTT\
""")

#Handle The '/ask'

@bot.message_handler(commands=['ask'])
def send_answer(message):
    question = message.text[len("/ask"):]
    
    if message.from_user.username in allowed_users:
        if len(question) == 0:
            bot.send_message(message.chat.id, "Send Like This: `/ask` Your Question")
        else:
            bot.send_message(message.chat.id, get_response(question))
    else:
        bot.send_message(message.chat.id, "Sorry, you are not authorized to use this bot.\nYou Want auth To Use This Bot \nAsk To Admins Here \n『sᴀᴛʏᴀᴍ』 : @Mr_majnu72 \nᴀᴍʙᴏᴛ : @AM_YTBOTT")


bot.infinity_polling()
