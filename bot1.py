import telebot
API_TOKEN = '7639450810:AAFAaYyjO5q6UDwB8ixcFrlo_vmBvCDuuD8'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()
