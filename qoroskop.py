from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,Dispatcher,CallbackQueryHandler
import requests
from telegram import InlineKeyboardMarkup,InlineKeyboardButton

updater = Updater(token="615469322:AAHY1NtnmN0cJ4p77-OYnN-7rgY1bWwedN8")
dispatcher = updater.dispatcher


def zodiacsigns(bot,update):
	options = [
			[InlineKeyboardButton("Aquarius",callback_data="Aquarius")],
			[InlineKeyboardButton("Pisces",callback_data="Pisces")],
			[InlineKeyboardButton("Aries",callback_data="Aries")],
			[InlineKeyboardButton("Taurus",callback_data="Taurus")],
			[InlineKeyboardButton("Gemini",callback_data="Gemini")],
			[InlineKeyboardButton("Cancer",callback_data="Cancer")],
			[InlineKeyboardButton("leo",callback_data="leo")],
			[InlineKeyboardButton("Virgo",callback_data="Virgo")],
			[InlineKeyboardButton("Libra",callback_data="Libra")],
			[InlineKeyboardButton("Scorpio",callback_data="Scorpio")],
			[InlineKeyboardButton("Sagittarius",callback_data="Sagittarius")],
			[InlineKeyboardButton("Capricorn",callback_data="Capricorn")]
				]
	reply = InlineKeyboardMarkup(options)
	bot.send_message(chat_id=update.message.chat_id,text="Please choose your Zodiac Signs: ",reply_markup=reply)

dispatcher.add_handler(CommandHandler("Signs", zodiacsigns))

def horoscopes(bot,update):
	data = update.callback_query.data
	text = "" 
	if (data == "Aqaurius"):
		# Aqua
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Aqaurius")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Pisces"):
		# Pisces
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Pisces")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Aries"):
		# Aries
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Aries")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Taurus"):
		# Taurus
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Taurus")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Gemini"):
		# Gemini
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Gemini")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Cancer"):
		# Cancer
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Cancer")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "leo"):
		# leo
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/leo")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Virgo"):
		# Virgo
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Virgo")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Libra"):
		# Libra
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Libra")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Scorpio"):
		# Scorpio
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Scorpio")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Sagittarius"):
		# Sagittarius
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Sagittarius")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	elif (data == "Capricorn"):
		# Capricorn
		req = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/Capricorn")
		text = req.json()["sunsign"]+"\n"+req.json()["horoscope"]+"\n"+"Today: "+req.json()["date"]
	bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
							text=text,message_id=update.callback_query.message.message_id)

dispatcher.add_handler(CallbackQueryHandler(horoscopes))

updater.start_polling()

updater.idle()