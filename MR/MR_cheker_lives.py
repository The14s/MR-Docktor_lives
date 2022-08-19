#by The14s_ 


from ast import main
from logging import Handler
from telegram.ext import Updater, ComandHandler
from  Helper import gsheet_helper

from cfg import TOKEN

def start(update, context):
    #print(update, message)
    name = update.message["from"]["username"]
    print(update.message["from"])
    update.message.repply_text(f"¡Felicidades!{name} Te has suscrito a ⚡️𝕄ᖇ.Ď𝓞Č𝐓𝐎ᖇᵇσт⚡️.
Usa /off para parar tu suscripción.")

def main():
    updater = Updater(Token, use_context=True)

    updater.dispatcher.add_handler(ComandHandler("start", start))

    # Start
    updater.strt_polling()
        print("Run")

        # Procesando
        updater.idle()


if __name__=="__maim__":
    main()        
    
