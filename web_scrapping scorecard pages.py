import csv
from bs4 import BeautifulSoup
import requests

# ارسال درخواست به URL و دریافت پاسخ
html_req = requests.get('https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-pakistan-final-1298179/full-scorecard')
soup = BeautifulSoup(html_req.text, 'lxml')
print(html_req)

# یافتن جدول بازیکنان
tables = soup.find_all('table')

# برای هر جدول، اطلاعات را استخراج کنید
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        # فیلتر کردن ردیف‌های مخفی
        if 'hidden' in row.get('class', []) or 'display:none' in row.get('style', ''):
            continue  # این ردیف را نادیده بگیر

        columns = row.find_all('td')
        if len(columns) >= 7:  # اطمینان از اینکه ردیف دارای حداقل 7 ستون است
            # فیلتر کردن ستون‌های مخفی
            if any('hidden' in col.get('class', []) or 'display:none' in col.get('style', '') for col in columns):
                continue  # این ردیف را نادیده بگیر

            player_name = columns[0].text.strip()
            r = columns[2].text.strip()
            b = columns[3].text.strip()
            m = columns[4].text.strip()
            fours = columns[5].text.strip()
            sixes = columns[6].text.strip()
            sr = columns[7].text.strip()
            
            # چاپ اطلاعات
            print(f"Player: {player_name}, R: {r}, B: {b}, M: {m}, 4s: {fours}, 6s: {sixes}, SR: {sr}")
            # print(f"Player: {player_name}, R: {r}, B: {b}, 4s: {fours}, 6s: {sixes}, SR: {sr}")
