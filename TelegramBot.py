import telebot
from GithubCrawler import GithubCrawler

bot = telebot.TeleBot("5444331349:AAEwF-iYda1HRmfWrFg7_lN6oDXU4l2fglk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def send_github_data(message):
    crawler = GithubCrawler()
    data = crawler.crawl(message.text)
    bot.send_message(data)

    
bot.infinity_polling()