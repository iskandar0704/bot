import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id,message.text)

GROUP_ID = '+ec8ccBLw6_RkMTFi'



@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url", "text_link"]: 
            # Мы можем не проверять chat.id, он проверяется ещё в хэндлере 
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return
	
bot.polling(none_stop=True)
