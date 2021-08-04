import setting
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен. Нажмите Ctrl+C для завершения")

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')
def start_bot(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, {}. Я Валютный бот".format(update.message.chat.first_name))


def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text)
		rate = 80.34
		rubl = number * rate
		message = "$%.2f = %.2f руб." % (number, rubl)
		context.bot.send_message(chat_id=chat.id, text=message)
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")

token = "1928110174:AAG0TAhy1l8KZvR-8yTCpXg4XYbGszwWefA"

updater = Updater(setting.TOKEN_TELEGRAM)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start_bot))
dp.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()

logging.info('Bot started!')
