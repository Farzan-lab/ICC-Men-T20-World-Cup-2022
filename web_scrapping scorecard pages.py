import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

# خواندن فایل CSV و ستون 'list'
file_path = "icc_t20_worldcup_2022_23_matches plus links.csv"
df = pd.read_csv(file_path)

# باز کردن فایل‌های CSV برای ذخیره اطلاعات
with open('player_batting.csv', 'w', newline='', encoding='utf-8') as batting_file, \
     open('player_bowling.csv', 'w', newline='', encoding='utf-8') as bowling_file:

    batting_writer = csv.writer(batting_file)
    bowling_writer = csv.writer(bowling_file)

    # نوشتن هدرها (ستون‌های فایل CSV)
    batting_writer.writerow(['Player', 'R', 'B', 'M', '4s', '6s', 'SR'])
    bowling_writer.writerow(['Player', 'O', 'M', 'R', 'W', 'Econ', '0s', '4s', '6s', 'wd', 'NB'])

    # فرض اینکه ستون 'link' حاوی لینک‌ها باشد
    for link in df['link']:
        # ارسال درخواست به URL (لینک فعلی از فایل CSV)
        html_req = requests.get(link)
        soup = BeautifulSoup(html_req.text, 'lxml')
        print(f"Fetching data from: {link}")

        tables = soup.find_all('table')

        # لیست‌های مربوط به جداول batting و bowling
        table_batting = []
        table_bowling = []

        table_batting.append(tables[0])
        table_bowling.append(tables[1])
        table_batting.append(tables[2])
        table_bowling.append(tables[3])

        # پردازش جدول batting
        for table in table_batting:
            rows = table.find_all('tr')
            for row in rows:
                if 'hidden' in row.get('class', []) or 'display:none' in row.get('style', ''):
                    continue  

                columns = row.find_all('td')
                if len(columns) >= 7:  
                    if any('hidden' in col.get('class', []) or 'display:none' in col.get('style', '') for col in columns):
                        continue  

                    player_name = columns[0].text.strip()
                    r = columns[2].text.strip()
                    b = columns[3].text.strip()
                    m = columns[4].text.strip()
                    fours = columns[5].text.strip()
                    sixes = columns[6].text.strip()
                    sr = columns[7].text.strip()

                    # ذخیره کردن اطلاعات در فایل player_batting.csv
                    batting_writer.writerow([player_name, r, b, m, fours, sixes, sr])

        # پردازش جدول bowling
        for table in table_bowling:
            rows = table.find_all('tr')
            for row in rows:
                if 'hidden' in row.get('class', []) or 'display:none' in row.get('style', ''):
                    continue  

                columns = row.find_all('td')
                if len(columns) >= 7:  
                    if any('hidden' in col.get('class', []) or 'display:none' in col.get('style', '') for col in columns):
                        continue  

                    player_name = columns[0].text.strip()
                    o = columns[1].text.strip()
                    m = columns[2].text.strip()
                    r = columns[3].text.strip()
                    w = columns[4].text.strip()
                    ECON = columns[5].text.strip() 
                    zero = columns[6].text.strip()
                    fourth = columns[7].text.strip()
                    sixth = columns[8].text.strip()
                    wd = columns[9].text.strip()
                    nb = columns[10].text.strip()

                    # ذخیره کردن اطلاعات در فایل player_bowling.csv
                    bowling_writer.writerow([player_name, o, m, r, w, ECON, zero, fourth, sixth, wd, nb])

print("Data saved to 'player_batting.csv' and 'player_bowling.csv'")
