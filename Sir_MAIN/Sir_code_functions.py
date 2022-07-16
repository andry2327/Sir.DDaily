import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import date
from datetime import datetime, timedelta
import imaplib
import email

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("SirDDaily-f846db1f3cca.json", scope)
creds1 = ServiceAccountCredentials.from_json_keyfile_name("_MyData-0d3082098eb9.json", scope)
creds2 = ServiceAccountCredentials.from_json_keyfile_name("Payments-1606ec843756.json", scope)
client = gspread.authorize(creds)
client1 = gspread.authorize(creds1)
client2 = gspread.authorize(creds2)
databse = client.open("Users databse").sheet1  # for users databse
mydata = client1.open("MyData").sheet1  # for users data
payments = client2.open("Payments").sheet1  # for payements

token = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telepot.Bot(token)

sdCoin = 1000  # 💠


def referral_reset(index, user_data):
    if index == 0:
        user_data[5] = str(0)  # F: 6, -> referral flag = 0
        user_data[6] = str(0)
    if index == 1:
        user_data[15] = str(0)
        user_data[13] = str(0)  # N: 14, -> withdraw flag = 0
        user_data[14] = str(0)  # O: 15, -> mail flag = 0


def i_user_finder(chat_id):
    global i_user
    index = 1
    n_users = mydata.cell(63, 24).value
    i_user_flag = 0
    user_list = databse.col_values(1)
    while (int(index) <= int(n_users)) and i_user_flag == 0:
        if int(chat_id) == int(user_list[index - 1]):
            i_user = index
            i_user_flag = 1
        else:
            index += 1
    if int(i_user_flag) == 0:
        i_user = int(i_user_flag)
    return i_user


def already_user_finder(chat_id):
    index = 1
    n_users = mydata.cell(63, 24).value
    already_user = 0
    user_list = databse.col_values(1)
    while int(index) <= int(n_users) and int(already_user) == 0:
        if int(chat_id) == int(user_list[index - 1]):
            already_user = 1
        else:
            index += 1
    return already_user


def user_finder_id(chat_id):
    index = 1
    n_users = mydata.cell(63, 24).value
    already_user = 0
    user_index = 0
    user_list = databse.col_values(1)
    while int(index) <= int(n_users) and int(already_user) == 0:
        if int(chat_id) == int(user_list[index - 1]):
            already_user = 1
            user_index = index
        else:
            index += 1
    return already_user, user_index


def is_mail(mail):
    if ('@' in mail) and ('.' in mail):
        return True
    else:
        return False


def is_btc_address(btc_address):
    if (len(btc_address) >= 26) and ((btc_address[0] == '1') or (btc_address[0] == '3') or (btc_address[0:3] == 'bc1')):
        return True
    else:
        return False


def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(chat_id, query_data)
    bot.answerCallbackQuery(query_id, text='Link is now active')
    i_this_user = i_user_finder(chat_id)
    databse.update_cell(i_this_user, 10, 1)  # J: 10  -> 1 step link flag = 1


def handle(msg):
    global messaggio
    n_users = mydata.cell(63, 24).value  # X: 24

    content_type, chat_type, chat_id = telepot.glance(msg)

    if not('username' in str(msg)):
        msg['from']['username'] = '[no_username]'

    if not('first_name' in str(msg)):
        msg['from']['first_name'] = '[no_first_name]'

    if not('last_name' in str(msg)):
        msg['from']['last_name'] = '[no_last_name]'

    if not('text' in str(msg)):
        msg['text'] = '[no_text]'

    print('\n' + str(chat_id) + '  ' + msg['from']['first_name'] + ' ' + msg['from']['last_name'] +
          '  (' + msg['from']['username'] + ',  ' + msg['from']['language_code'] + ');   '
                                                                                   ' text: [' + msg['text'] + ']')

    link_list = ['https://up-to-down.net/134238/ggg', 'https://dausel.co/YJDhOb', 'https://iir.ai/WW04FGb',
                 'https://shrinke.me/zf7cbIzg',  'https://tii.ai/pFwCHsm7', 'https://uiz.io/P6tJ6',
                 'https://cpmlink.net/WUdlAQ', 'http://clik.pw/E1E7d', 'https://lnkload.com/2stmf',
                 'http://adfoc.us/52268175665939', 'http://raboninco.com/2BWiP', 'https://payskip.org/BIPktnQYXY',
                 'https://aii.sh/MlK3ft', 'https://ouo.io/jcGzeC', 'https://smoner.com/jWhEGs', 'http://uii.io/VaCRR',
                 'http://bc.vc/2nx43LS', 'https://stfly.me/kPB8xNU', 'https://oke.io/krVmH7',
                 'http://gestyy.com/eeEcsW', 'http://raboninco.com/2BWkI', 'http://gestyy.com/eeEcfb',
                 'https://ouo.io/HzKTsdN', 'http://bc.vc/JRpEKtz', 'https://dausel.co/sCVVN8',
                 'https://cpmlink.net/XUdlAQ', 'http://clik.pw/2TNLs',
                 'https://lnkload.com/2stmh', 'http://adfoc.us/53192075778893', 'https://direct-link.net/149822/gggg',
                 'https://iir.ai/vWg4JNV', 'https://aii.sh/CvFVqDyf', 'https://shrinke.me/OOMk',
                 'https://smoner.com/9xPLO', 'http://uii.io/YRogDL2', 'https://tii.ai/qRf76jt', 'https://oke.io/coRn',
                 'https://uiz.io/tc1E', 'http://raboninco.com/2BWml', 'http://gestyy.com/eeEch8',
                 'https://ouo.io/47hXMP', 'http://bc.vc/K3yeEZf', 'https://dausel.co/cgcmmR',
                 'https://cpmlink.net/ZEdlAQ', 'http://clik.pw/2TNLs', 'https://lnkload.com/2stmk',
                 'http://adfoc.us/53234475787495', 'https://link-to.net/150078/ggg', 'https://iir.ai/T3ATp9xJ',
                 'https://aii.sh/pZx64', 'https://shrinke.me/79lzK', 'https://smoner.com/l2UWrofb',
                 'http://uii.io/BGtU', 'https://tii.ai/5o3bX', 'https://stfly.me/3qwjbEd', 'https://oke.io/DmY7Z1Io',
                 'https://uiz.io/tvc40']

    if content_type == 'text':
        messaggio = msg['text']
    else:
        messaggio = '[no_text]'

    if messaggio == "/start":
        if int(already_user_finder(chat_id)) == 0:
            bot.sendMessage(chat_id,
                            'Hi!👋\n'
                            'This is Sir.DDaily bot.\n'
                            'You can earn free money using me.'
                            '\nUse /howto command to learn how to use me.\n\n'
                            'Enjoy!🤑')
            row = [chat_id, msg['from']['first_name'] + ' ' + msg['from']['last_name'], '0', '0', '', '0', '0', '0', '',
                   '0', '0', '', '0', '0', '0', '0', '', str(datetime.now() - timedelta(days=1))]
            databse.insert_row(row, int(n_users) + 1)
            mydata.update_cell(63, 24, int(n_users) + 1)

    i_user = i_user_finder(chat_id)
    user_data = databse.row_values(i_user)

    if (messaggio == "🔍 Link") or (messaggio == "/link"):
        sleep(0.1)
        if int(user_data[2]) == 0:
            if (datetime.now() - datetime(int(user_data[17][0:4]), int(user_data[17][5:7]), int(user_data[17][8:10]),
                                          int(user_data[17][11:13]), int(user_data[17][14:16]),
                                          int(user_data[17][17:19]))).total_seconds() > 86400:
                bot.sendMessage(chat_id,
                                'Here is your link:\n\n'
                                '⚠️ OPEN IT IN YOUR BROWSER APP, not in telegram browser, to avoid any problems',
                                reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                    [InlineKeyboardButton(text="Open link ▶️", url=link_list[int(user_data[2])])]
                                ]))
                user_data[17] = str(datetime.now())
                user_data[2] = str(int(user_data[2]) + 1)
                user_data[9] = str(1)  # J: 10  -> 1 step link flag = 1
            else:
                time_left = int(86400 - (datetime.now() - datetime(int(user_data[17][0:4]), int(user_data[17][5:7]),
                                                                   int(user_data[17][8:10]), int(user_data[17][11:13]),
                                                                   int(user_data[17][14:16]),
                                                                   int(user_data[17][17:19]))).total_seconds())
                bot.sendMessage(chat_id, 'You finished your links for today! Come back again in\n' + str(
                    int(time_left / 3600)) + ' hours and ' + str(
                    int((time_left - int(time_left / 3600) * 3600) / 60)) + ' min')

        else:
            bot.sendMessage(chat_id,
                            'Here is your link:\n\n'
                            '⚠️ OPEN IT IN YOUR BROWSER APP, not in telegram built to avoid any problems',
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="2. Open link ▶️", url=link_list[int(user_data[2])])]
                            ]))
            user_data[2] = str(int(user_data[2]) + 1)
            user_data[9] = str(1)  # J: 10  -> 1 step link flag = 1

        if int(user_data[2]) == 57:
            user_data[2] = str(0)

    elif (messaggio == "💸 Withdraw") or (messaggio == "/withdraw"):
        if float(user_data[3].replace(',', '.')) <= 0.15:
            bot.sendMessage(chat_id, "You don't have enough sdCoin💠\nCheck your /balance")
        else:
            bot.sendMessage(chat_id, "Insert the amount you want to withdraw:\n (>150)")
            user_data[13] = str(1)  # N: 14, -> withdraw flag = 1

    elif messaggio.isdigit() and int(user_data[13]) == 1:
        if float(messaggio.replace(',', '.')) > float(user_data[3].replace(',', '.')) * sdCoin:
            bot.sendMessage(chat_id, "You don't have enough sdCoin💠\nCheck your /balance")
            user_data[13] = str(0)  # N: 14, -> withdraw flag = 0
        else:
            if float(messaggio.replace(',', '.')) >= 0.15*sdCoin:
                bot.sendMessage(chat_id, "Perfect! Now write your PayPal e-mail or your Bitcoin address:\n"
                                         "(Check that you write it correctly)")
                user_data[15] = float(messaggio) / 1000  # O: 15, -> amount withdrawned
                user_data[14] = str(1)  # O: 15, -> mail flag = 1
            else:
                bot.sendMessage(chat_id, "Remember that amount must be >150")

    elif (is_mail(messaggio) or is_btc_address(messaggio)) and (int(user_data[13]) == 1) and (int(user_data[14]) == 1):
        bot.sendMessage(chat_id,
                        'Success! Your money will be sent as soon as possible!\n\n'
                        'Check /contact if you have any questions or problems')
        new_balance = float(user_data[3].replace(',', '.')) - float(user_data[15].replace(',', '.'))
        user_data[3] = str(new_balance)
        today = date.today()
        now = datetime.now()
        payment_row = [chat_id,  today.strftime("%d %b %Y") + '   '
                       + now.strftime("%H:%M"), msg['from']['username'],
                       messaggio, float(user_data[15].replace(',', '.'))]
        payments.insert_row(payment_row, 1)  # add row payement
        user_data[15] = str(0)
        user_data[13] = str(0)  # N: 14, -> withdraw flag = 0
        user_data[14] = str(0)  # O: 15, -> mail flag = 0

    elif (messaggio == "💰 Balance") or (messaggio == "/balance"):
        balance1 = float((user_data[3]).replace(',', '.'))
        balance = round(balance1, 6)
        bot.sendMessage(chat_id, 'Your current balance is: ' + str(balance * sdCoin) + ' sdCoin💠')

    elif messaggio == "/contact":
        bot.sendMessage(chat_id,
                        'If you have any questions or problems don’t hesitate to contact me on IG: @sir.ddaily \n\n'
                        'https://instagram.com/sir.ddaily?igshid=1hc31658q7us8')

    elif messaggio == "/referral":
        bot.sendMessage(chat_id, 'If you have referral type "Y"')
        user_data[5] = str(1)  # F: 6, -> referral flag = 1

    elif messaggio == "/myid":
        bot.sendMessage(chat_id, 'your ID is: ' + str(chat_id))

    elif messaggio == "/commandlist":
        bot.sendMessage(chat_id,
                        '/howto - how to use this bot \n'
                        ' /contact - contact me if you have any questions or problems\n '
                        '/commandlist - here’s the command list \n '
                        '/referral - if you have any referral, use this command (1 each user) \n '
                        '/myid - check your ID here\n\n'
                        'Buttons: \n\n'
                        '[🔍 Link] - using this button, you’ll get a new link \n'
                        ' [💰 Balance] - you can see your current balance \n'
                        ' [💸 Withdraw] - you can withdraw your incomes\n\n'
                        'If you can’t see the keyboard buttons, use this commands instead:\n\n'
                        '/link ([🔍Link])\n'
                        '/balance ([💰 Balance])\n'
                        '/withdraw ([💸 Withdraw])')

    elif messaggio == "/howto":
        bot.sendMessage(chat_id, '1. Use the [🔍Link] button to recive a new link\n'
                                 '2. click the [Open link here ▶️] button to access the website\n'
                                 '3. You have to watch some ads and then skip them\n'
                                 '4. Once you skipped all ads you’ll get to a web page, usually called “ddgamesirylw”\n'
                                 '5. Write your ID in the input box at bottom-right of the page, '
                                 'then click “Send” (you can find your ID with /myid command)\n'
                                 '6. Get your revenue!\n\n'
                                 'IMPORTANT:\n\n'
                                 'The [💸Withdraw] button lets you send your money to your PayPal account '
                                 'and Bitcoin wallet, once you have reached 150 SDcoin ( 1000 SDcoin = 1 €).\n'
                                 'Use /contact if you need help\n\n'
                                 '⚠️⚠️VERY IMPORTANT⚠️⚠️:\n\n'
                                 'You want to earn even more?\n'
                                 'You can share this bot with 5 of your friends and '
                                 'if they write your ID using the /referral command, '
                                 'you will earn up to 40% more from every of your earnings!🤩🤩\n\n'
                                 'Enjoy!')

    elif messaggio == "Y":
        already_referral_flag = int(user_data[12])  # M:13 -> Already referral flag
        if already_referral_flag == 0:
            if int(user_data[5]) == 1:
                bot.sendMessage(chat_id, 'Insert your friend ID referral:')
                user_data[6] = str(1)  # G: 7, -> referral flag = 1
        else:
            bot.sendMessage(chat_id, 'You already inserted your referral!')
            user_data[5] = str(0)  # F: 6, -> referral flag = 0
            user_data[6] = str(0)  # G: 7, -> Y flag = 0

    elif messaggio.isdigit() and int(user_data[5]) == 1 and int(user_data[6]) == 1:  #
        i_ref = i_user_finder(int(messaggio))
        if i_ref == 0:
            bot.sendMessage(chat_id, 'Sorry, user not Found\nCheck that your friend ID is correct')
        else:
            if int(messaggio) != int(chat_id):
                bot.sendMessage(chat_id, 'Success!🤩\nYour friend will now earn 40% more from every earning')
                databse.update_cell(int(i_ref), 8, int(databse.cell(int(i_ref), 8, ).value) + 1)
                user_data[12] = str(1)  # M:13 -> Already referral flag = 1
                user_data[5] = str(0)  # F: 6, -> referral flag = 0
                user_data[6] = str(0)  # G: 7, -> y flag = 0

            else:
                bot.sendMessage(chat_id, "Nice try, but that doesn't work 😉")
                referral_reset(0, user_data)

    elif messaggio == "Why are you gay?":
        bot.sendMessage(chat_id, "Who says I'm gay?")

    if (messaggio.isdigit() is False) and (int(user_data[5]) == 1) and (messaggio != "Y" and messaggio != "/referral"):
        referral_reset(0, user_data)

    if (messaggio.isdigit() is False) and (int(user_data[13]) == 1) and (messaggio != "/withdraw") and \
            (messaggio != "💸 Withdraw") and ('@' not in messaggio) and ('.' not in messaggio):
        referral_reset(1, user_data)

    if messaggio != "/start":
        databse.delete_rows(i_user)
        if int(user_data[9]) == 1:
            if (messaggio != "/link") and (messaggio != "🔍 Link"):
                user_data[9] = str(0)
        databse.insert_row(user_data, i_user)

    print(user_data)


def get_inbox():
    host = 'imap.gmail.com'
    username = 'YOUR_MAIL'
    password = 'YOUR_MAIL_PASSWORD'

    mail_body = 'NULL'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
                mail_body = email_data['body']
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
                mail_body = email_data['html_body']
        my_message.append(email_data)
    return mail_body
