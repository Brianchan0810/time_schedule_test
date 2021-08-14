import pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import date, datetime

gc = pygsheets.authorize(service_file='json_keyfile.json')
scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#creds = ServiceAccountCredentials.from_json_keyfile_name('json_keyfile.json', scope)

sheet_id = '104z9SpogCFx-5yUy5uzZH1nfmuRU5ppLzzZmaCMIdn4'

sh  =gc.open_by_key(sheet_id)
wk1 = sh[0]
wk1.update_value('B5', 'I am brian hihi ')



my_sheet_id = '1OcDHd4YkhQKgPpPEmdqJCqAW8hY2amXLsfudzhrFB8o'
shit  =gc.open_by_key(my_sheet_id)
my_wk1 = shit[0]
my_wk1.update_value('B5', 'I am brian hihi ')
today_date = date.today()
current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(current_time)
print(today_date)
my_wk1.update_value('B7',str(today_date))