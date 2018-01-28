import telegram

 
token_samm = "336120290:AAH4gV1OtyYgvdpmR_Hk7W7cSBrapM05HbY"
chat_id='27813608'

bot = telegram.Bot(token=token_samm)
status = bot.send_message(chat_id=chat_id, text="Hola")
 
print(status)