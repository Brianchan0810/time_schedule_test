import pygsheets
from datetime import date, datetime

gc = pygsheets.authorize(service_file='json_keyfile.json')
sheet_id = '1OcDHd4YkhQKgPpPEmdqJCqAW8hY2amXLsfudzhrFB8o'

sheet = gc.open_by_key(sheet_id)
wk1 = sheet[0]
first_empty_row_num = len(list(filter(None,wk1.get_col(1))))+1
print(first_empty_row_num)

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

wk1.update_value(f'A{first_empty_row_num}', current_time)
wk1.update_value(f'B{first_empty_row_num}', 'hihihi')
