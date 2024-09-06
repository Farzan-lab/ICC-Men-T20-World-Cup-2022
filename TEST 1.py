import csv
from bs4 import BeautifulSoup
import requests

html_req = requests.get('https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-pakistan-final-1298179/full-scorecard')
soup = BeautifulSoup(html_req.text, 'lxml')
print(html_req)

tables = soup.find_all('table')
table = tables[0]
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
            
        print(f"Player: {player_name}, R: {r}, B: {b}, M: {m}, 4s: {fours}, 6s: {sixes}, SR: {sr}")
#-----------------------
table = tables[1]
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

        # WD = columns[9].text.strip()
            
        print(f"Player: {player_name}, R: {o}, B: {m}, M: {r}, w: {w}, Econ: {ECON}, 0s: {zero}, 4s: {fourth}, 6s: {sixth}, wd: {wd}, NB: {nb}")

#--------------------------

table = tables[2]
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
            
        print(f"Player: {player_name}, R: {r}, B: {b}, M: {m}, 4s: {fours}, 6s: {sixes}, SR: {sr}")

#-----------------------
table = tables[3]
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

        # WD = columns[9].text.strip()
            
        print(f"Player: {player_name}, R: {o}, B: {m}, M: {r}, w: {w}, Econ: {ECON}, 0s: {zero}, 4s: {fourth}, 6s: {sixth}, wd: {wd}, NB: {nb}")
