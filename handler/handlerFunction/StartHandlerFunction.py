from telegram import Update, KeyboardButton, KeyboardButtonPollType
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import handler.handlerModel.InformationHandlerModel as StartHandlerModel
message = StartHandlerModel.StartMessage()
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text( text=message)

