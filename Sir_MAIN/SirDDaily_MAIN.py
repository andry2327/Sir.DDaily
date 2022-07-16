from Sir_code_functions import token
from Sir_code_functions import handle, on_callback_query
import telepot
from telepot.loop import MessageLoop
from time import sleep

bot = telepot.Bot(token)

MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()

while 1:
    sleep(2)
