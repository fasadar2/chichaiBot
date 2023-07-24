from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import handler.handlerModel.InformationHandlerModel as StartHandlerModel

message = StartHandlerModel.HelpMessage()
async def help(update:Update,context:ContextTypes.DEFAULT_TYPE):

    button = [[KeyboardButton("/help")], [KeyboardButton("/bookNow")],[KeyboardButton("/mark")],[KeyboardButton("/statistic")]]
    await update.effective_message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True,resize_keyboard=True)
    )