from telegram import Update
import handler.HandlersBuilder as handlers
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import TelegramObject
if __name__ == '__main__':
    aplication = ApplicationBuilder().token('6333189100:AAEEsML_0LPCMzdKGkm-xGql3uxmYHBQ__E').build()
    print("Bot started")
    aplication.add_handlers(handlers.CreateHandler())
    aplication.run_polling()


