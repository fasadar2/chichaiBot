from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def statistic(update:Update,context:ContextTypes.DEFAULT_TYPE):

    button = [[KeyboardButton("/userStatistic")], [KeyboardButton("/allStatistic")]]
    message = "тут вы можете посмотреть статистику"
    await update.effective_message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True,resize_keyboard=True)
    )
async def userStatistic(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message = "статистика n-пользователя"
    await update.effective_message.reply_text(
        message
    )
async def allStatistic(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message = "статистика всех пользователей"
    await update.effective_message.reply_text(
        message
    )