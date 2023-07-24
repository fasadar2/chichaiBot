from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def mark(update:Update,context:ContextTypes.DEFAULT_TYPE):
    button = [[KeyboardButton("/markRead")], [KeyboardButton("/markReadToday")]]
    message = "что вы сегодня сделали ? "
    await update.effective_message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True, resize_keyboard=True)
    )

async def markAsReadToday(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message = "тут будет собщение о том что вы читали сегодня"
    await update.effective_message.reply_text( text=message)
async def markAsRead(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message = "тут будет собщение о том что вы закончили чтение"
    await update.effective_message.reply_text( text=message)