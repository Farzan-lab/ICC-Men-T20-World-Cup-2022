import csv
from bs4 import BeautifulSoup
import requests

# ارسال درخواست به URL و دریافت پاسخ
html_req = requests.get('https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450')
soup = BeautifulSoup(html_req.text, 'lxml')

# ایجاد و باز کردن فایل CSV برای نوشتن
with open('icc_t20_worldcup_2022_23_matches.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # نوشتن هدرها (ستون‌های فایل CSV)
    csvwriter.writerow(['Team 1', 'Team 2', 'Winner', 'Margin', 'Ground', 'Match Date', 'Scorecard'])

    # تیم‌ها و اطلاعات مربوطه را استخراج کرده و در فایل CSV ذخیره کنید
    tags = soup.find_all('tr', class_="ds-bg-ui-fill-translucent")
    
    for tag in tags:
        teams = tag.find_all('td', class_="ds-min-w-max")
        if len(teams) >= 7:  # بررسی اینکه آیا تعداد ستون‌ها کافی است
            team1 = teams[0].find('span').text.strip()
            team2 = teams[1].find('span').text.strip()
            winner = teams[2].text.strip()  # ستون سوم مربوط به برنده است
            margin = teams[3].text.strip()  # ستون چهارم مربوط به حاشیه (Margin) است
            ground = teams[4].text.strip()  # ستون پنجم مربوط به مکان بازی است
            match_date = teams[5].text.strip()  # ستون ششم مربوط به تاریخ بازی است
            scorecard = teams[6].find('a')['href']  # لینک نمره
            
            # چاپ تیم‌ها و برنده (اختیاری)
            print(team1, '/', team2, '/', winner, '/', margin, '/', ground, '/', match_date, '/', scorecard)
            
            # نوشتن داده‌ها در فایل CSV
            csvwriter.writerow([team1, team2, winner, margin, ground, match_date, scorecard])
    print("********tip2*************")
    tags = soup.find_all('tr', class_ ="")

    for tag in tags: 
        teams= tag.find_all('td',class_="ds-min-w-max")
        team1 = teams[0].find('span').text.strip()
        team2 = teams[1].find('span').text.strip()
        winner = teams[2].find('span').text.strip()
        Margin = teams[3].find('span').text.strip()
        Ground = teams[4].find('span').text.strip()
        Match_date = teams[5].find('span').text.strip()
        scorecard = teams[6].find('span').text.strip()
        print(team1,'/',team2,'/',winner,'/',Margin,'/',Ground,'/',Match_date,'/',scorecard)
        csvwriter.writerow([team1, team2, winner, Margin, Ground, Match_date, scorecard])

print("Data has been saved to 'icc_t20_worldcup_2022_23_matches.csv'.")
