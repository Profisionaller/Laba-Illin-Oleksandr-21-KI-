import telebot
API_TOKEN = '7639450810:AAFAaYyjO5q6UDwB8ixcFrlo_vmBvCDuuD8'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Це бот!")
@bot.message_handler(func=lambda _: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
