from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here

owm = OWM('ee538c520c50def6b878e3a9480470a4', config_dict)
bot = telebot.TeleBot("1133866404:AAH1yWMp2tRaA_ViIp7RE4vD5d2xXOI6P_8")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	
    
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place( message.text )
    
    w = observation.weather    
    
    w.temperature('celsius')

    
    temp = w.temperature ('celsius')["temp"] 
    
    answer = "В городе " + message.text + " Сейчас " + str (w.detailed_status) + "\n"
    
    answer += "Температура сейчас примерно" + str(temp) + "\n"

    
    if temp < 10:
        answer += "Сейчас оч холодно, одень куртку мудачело"
    elif temp < 20:
        answer += "Ну типло типло но лучше бы ты оделся потеплее бурурич емае"
    else:
        answer += "А вот ща самое то чтобы в одних трусах проветрить свои яйца!!!"          	
    

    bot.send_message(message.chat.id,answer)

bot.polling( none_stop= True )