startMessage = "Я великий мастер ЧичЧая. " \
              "Мою возможности безграничны. " \
              "Вот некоторые из них: \n"
helpMessage = "/help - здесь ты узнаешь все мои комманды \n" \
              "/startChiChai -  здесь ты запустишь меня \n" \
              "/bookNow - узнать текущую книгу \n" \
              "/mark - отметить книгу \n" \
              "/markReadToday - отметить чтение книги \n" \
              "/markRead - отметить прочтение книги \n" \
              "/statistic - посмотреть статистику \n" \
              "/allStatistic - посмотреть всю статистику \n" \
              "/userStatistic - посмотреть статистику"
def HelpMessage():
        return helpMessage
def StartMessage():
        return startMessage + helpMessage




