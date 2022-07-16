from datetime import datetime, timedelta
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mydata stats reset-2abb99e36037.json", scope)
client = gspread.authorize(creds)
MyData_reset = client.open("MyData").sheet1  # for MyData reset

while 1:
    if str(datetime.now())[11:16] == '00:00':
        now_date1 = datetime.now() - timedelta(days=1)
        now_date = str(now_date1)[8:10] + ' / ' + str(now_date1)[5:7] + ' / ' + str(now_date1)[0:4]
        stat_update = ['', '', '', '', '', '', '', '', str(now_date), '..' + str(MyData_reset.cell(61, 4).value),
                       '..' + str(MyData_reset.cell(61, 5).value)]
        day_i = int(MyData_reset.cell(61, 9).value)
        MyData_reset.insert_row(stat_update, day_i)
        sleep(1)
        i = 1
        while i <= 57:
            MyData_reset.update_cell(i, 4, 0)
            i += 1
            sleep(2)

        MyData_reset.update_cell(61, 9, str(day_i + 1))

        if str(datetime.now())[8:10] == '01':
            now_date1 = datetime.now()
            now_date = str(int(str(now_date1)[6:7]) - 1) + ' / ' + str(now_date1)[0:4]
            day_i = int(MyData_reset.cell(61, 13).value)
            MyData_reset.update_cell(day_i, 13, now_date)
            MyData_reset.update_cell(day_i, 14, '..' + str(MyData_reset.cell(61, 6).value))
            MyData_reset.update_cell(day_i, 15, '..' + str(MyData_reset.cell(61, 7).value))
            sleep(1)
            j = 1
            while j <= 57:
                MyData_reset.update_cell(j, 6, 0)
                j += 1
                sleep(2)

            MyData_reset.update_cell(61, 13, str(day_i + 1))
    sleep(2)
