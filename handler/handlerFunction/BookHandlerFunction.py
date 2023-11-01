from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import handler.handlerModel.InformationHandlerModel as StartHandlerModel
from model import *
from model.BookModel import BookModel


async def Getbook(update:Update,context:ContextTypes.DEFAULT_TYPE):
    cur_query = BookModel.select().limit(2)
    data = cur_query.dicts().execute()
    data = data[0]
    name = data["name"]
    author = data["author"]
    description = data["description"]
    url = data["url_book"]
    message = f"Книга:{name}\nАвтор: {author}\n{description}\nскачать в:{url}"
    await update.effective_message.reply_text(text=message)



