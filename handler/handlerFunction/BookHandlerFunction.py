from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import handler.handlerModel.InformationHandlerModel as StartHandlerModel
message = "тут будет описание книги"
async def Getbook(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(text=message)