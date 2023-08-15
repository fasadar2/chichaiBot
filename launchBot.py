from telegram import Update
import handler.HandlersBuilder as handlers
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import TelegramObject
if __name__ == '__main__':
    aplication = ApplicationBuilder().token(settings.token).build()
    print("Bot started")
    aplication.add_handlers(handlers.CreateHandler())
    aplication.run_polling()


