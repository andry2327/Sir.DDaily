from time import sleep
from Sir_code_functions import get_inbox
from Sir_code_functions import user_finder_id
from Sir_code_functions import token
from Sir_code_functions import sdCoin
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import telepot

bot = telepot.Bot(token)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("SirDDaily-f846db1f3cca.json", scope)
creds1 = ServiceAccountCredentials.from_json_keyfile_name("_MyData-0d3082098eb9.json", scope)
client = gspread.authorize(creds)
client1 = gspread.authorize(creds1)
databse = client.open("Users databse").sheet1  # for users databse
mydata = client1.open("MyData").sheet1  # for users data

Link_Revenue_List = mydata.col_values(3)

while 1:
    inputbox_value = get_inbox()
    if inputbox_value != 'NULL':
        if_user_flag, user_index = user_finder_id(inputbox_value)
        if if_user_flag == 1:
            user_row = databse.row_values(user_index)
            print('\n')
            if int(user_row[9]) == 1:  # J:10 -> 1 step link flag check
                full_revenue = float((Link_Revenue_List[int(user_row[2])]).replace(',', '.'))
                if int(user_row[7]) <= 5:
                    mly = 0.5
                else:
                    mly = 0.7
                user_revenue = round((float(full_revenue*mly*sdCoin)), 6)
                bot.sendMessage(int(user_row[0]),
                                'You earned ' + str(user_revenue) + ' sdCoin💠 for visiting last website 👊🏼\n\n'
                                'Click /link or the button [🔍Link] for a new one')
                linkamount1 = int(mydata.cell(int(user_row[2]), 4).value) + 1  # update di mydata +1
                linkamount2 = int(mydata.cell(int(user_row[2]), 6).value) + 1  # link cell is ALREADY +1
                mydata.update_cell(int(user_row[2]), 4, linkamount1)               #
                mydata.update_cell(int(user_row[2]), 6, linkamount2)               #
                user_row[3] = float((user_row[3]).replace(',', '.')) + float(full_revenue*mly)
                user_row[9] = str(0)
                databse.delete_rows(user_index)
                databse.insert_row(user_row, user_index)
            else:
                bot.sendMessage(int(user_row[0]), "Nice try, but that doesn't work 😉")
    sleep(0.5)
