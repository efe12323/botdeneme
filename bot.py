import telebot
import requests

# Telegram botunuzun tokenını buraya girin
TOKEN = "6473719227:AAFBCIuXLcAveb_6uEDWVI5cQWABBXjEDsU"

# Telebot objesini oluşturun
bot = telebot.TeleBot(TOKEN)

# Döviz API'sinin URL'si
API_URL = "https://api.exchangerate-api.com/v4/latest/TRY"  # Türk Lirası (TRY) kullandık

# Döviz verilerini almak için fonksiyon
def get_exchange_rate(currency):
    response = requests.get(API_URL)
    data = response.json()
    if currency.upper() in data["rates"]:
        return data["rates"][currency.upper()]
    else:
        return None

# /start komutuna yanıt veren fonksiyon
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Merhaba! Ben bir döviz botuyum. Döviz adını yazarak anlık döviz kurlarını alabilirsiniz.")

# Döviz adı mesajı alındığında bu fonksiyon çalışır
@bot.message_handler(func=lambda message: True)
def get_currency(message):
    currency = message.text
    rate = get_exchange_rate(currency)
    if rate:
        bot.reply_to(message, f"1 TRY = {rate} {currency.upper()}")
    else:
        bot.reply_to(message, "Geçersiz döviz adı. Lütfen tekrar deneyin.")

# Botu çalıştırın
bot.polling()
