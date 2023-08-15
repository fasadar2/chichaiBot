from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import handler.handlerModel.InformationHandlerModel as StartHandlerModel
from model import *
from model.BookModel import BookModel

message = "тут будет описание книги"
async def Getbook(update:Update,context:ContextTypes.DEFAULT_TYPE):
    cur_query = BookModel.select().limit(5)
    for item in cur_query.dicts().execute():
        print('book: ', item)
    await update.effective_message.reply_text(text=message)