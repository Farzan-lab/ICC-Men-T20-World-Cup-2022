import csv
from bs4 import BeautifulSoup

import requests

# creating csv file
with open('icc_t20_worldcup_2022_23_matches.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # نوشتن هدرها (ستون‌های فایل CSV)
    csvwriter.writerow(['Team 1', 'Team 2', 'Winner', 'Margin', 'Ground', 'Match Date', 'Scorecard'])



html_req = requests.get('https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450')
soup = BeautifulSoup(html_req.text, 'lxml')
#teams
tags = soup.find_all('tr', class_ ="ds-bg-ui-fill-translucent")
# team 1
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


#     team1 = match.find("span").text.replace(" ", "")
#     match1= tag.find('td', class_="ds-min-w-max ds-text-right")
#     teams2 = match1.find("span").text.replace(" ", "")

# #winner


# # margin  

    
#     print(team1,":", teams2) 

    

