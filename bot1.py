from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
 
token = "7639450810:AAFAaYyjO5q6UDwB8ixcFrlo_vmBvCDuuD8"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши мені щось не будь")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)


def main():

    application = ApplicationBuilder().token(token).build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    application.run_polling()

if __name__ == "__main__":
    main()
