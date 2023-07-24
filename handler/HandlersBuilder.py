from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from handler.handlerFunction import BookHandlerFunction,\
    StartHandlerFunction,\
    HelpHandlerFunction,\
    MarkHandlerFunction,\
    StatisticHandlerFunction


def  CreateHandler():
    handlerList = []
    startHandler = CommandHandler("startChiChai",StartHandlerFunction.start)
    helpHandler = CommandHandler("help",HelpHandlerFunction.help)
    bookHandler = CommandHandler("bookNow",BookHandlerFunction.Getbook)
    markHandler = CommandHandler("mark",MarkHandlerFunction.mark)
    markReadTodayHandler = CommandHandler("markReadToday", MarkHandlerFunction.markAsReadToday)
    markReadHandler = CommandHandler("markRead",MarkHandlerFunction.markAsRead)
    statisticHandler = CommandHandler("statistic",StatisticHandlerFunction.statistic)
    userStatisticHandler = CommandHandler("userStatistic",StatisticHandlerFunction.userStatistic)
    allStatisticHandler = CommandHandler("allStatistic", StatisticHandlerFunction.allStatistic)

    handlerList.append(startHandler)

    handlerList.append(helpHandler)

    handlerList.append(bookHandler)

    handlerList.append(markHandler)
    handlerList.append(markReadHandler)
    handlerList.append(markReadTodayHandler)

    handlerList.append(statisticHandler)
    handlerList.append(userStatisticHandler)
    handlerList.append(allStatisticHandler)

    return handlerList